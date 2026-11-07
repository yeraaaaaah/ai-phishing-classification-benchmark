import json
import numpy as np
import pandas as pd


def load_raw_data(filepath: str) -> pd.DataFrame:
  """Loads raw jsonl logs into pandas DataFrame."""
  records = []
  with open(filepath, 'r', encoding='utf-8') as f:
    for line in f:
      if line.strip():
        records.append(json.loads(line))
  return pd.DataFrame(records)


def filter_warmup(df: pd.DataFrame) -> pd.DataFrame:
  """Filters out cold-start warm-up samples."""
  return df[df['is_warmup'] == False].copy()


def compute_bootstrap_ci(data, n_bootstraps=1000, ci=95, seed=42):
  """Calculates non-parametric bootstrap confidence interval."""
  np.random.seed(seed)
  boot_means = []
  n = len(data)
  for _ in range(n_bootstraps):
    sample = np.random.choice(data, size=n, replace=True)
    boot_means.append(np.mean(sample))
  lower = np.percentile(boot_means, (100 - ci) / 2)
  upper = np.percentile(boot_means, 100 - (100 - ci) / 2)
  return lower, upper


def aggregate_metrics(df: pd.DataFrame) -> pd.DataFrame:
  """Calculates medians, percentiles, 95% CIs and guardrail metrics."""
  summary_rows = []
  for model_type, group in df.groupby('model_type'):
    latencies = group['latency_ms'].values
    accuracies = group['accuracy'].values * 100.0  # Percentage

    lat_ci_low, lat_ci_high = compute_bootstrap_ci(latencies)
    acc_ci_low, acc_ci_high = compute_bootstrap_ci(accuracies)

    summary_rows.append({
        'model_type': model_type,
        'sample_count': len(group),
        'latency_mean_ms': np.mean(latencies),
        'latency_std_ms': np.std(latencies),
        'latency_median_ms': np.median(latencies),
        'latency_p25_ms': np.percentile(latencies, 25),
        'latency_p75_ms': np.percentile(latencies, 75),
        'latency_p95_ms': np.percentile(latencies, 95),
        'latency_p99_ms': np.percentile(latencies, 99),
        'latency_ci95_low_ms': lat_ci_low,
        'latency_ci95_high_ms': lat_ci_high,
        'accuracy_mean_pct': np.mean(accuracies),
        'accuracy_std_pct': np.std(accuracies),
        'accuracy_median_pct': np.median(accuracies),
        'accuracy_p25_pct': np.percentile(accuracies, 25),
        'accuracy_p75_pct': np.percentile(accuracies, 75),
        'accuracy_ci95_low_pct': acc_ci_low,
        'accuracy_ci95_high_pct': acc_ci_high,
        'fp_rate_pct': np.mean(group['fp_rate']) * 100.0,
        'error_rate_pct': np.mean(group['error_flag']) * 100.0,
    })
  return pd.DataFrame(summary_rows)


if __name__ == '__main__':
  import os

  data_path = (
      'data/raw/test_run.jsonl'
      if os.path.exists('data/raw/test_run.jsonl')
      else '../data/raw/test_run.jsonl'
  )
  out_path = (
      'data/processed/metrics_summary.csv'
      if os.path.exists('data')
      else '../data/processed/metrics_summary.csv'
  )

  raw_df = load_raw_data(data_path)
  eval_df = filter_warmup(raw_df)
  summary_df = aggregate_metrics(eval_df)
  summary_df.to_csv(out_path, index=False)
  print(f'Processed metrics saved to {out_path}')