import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('seaborn-v0_8-paper')
sns.set_palette('colorblind')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'figure.autolayout': True,
})


def plot_latency_vs_load(df: pd.DataFrame, output_dir: str = 'reports/figures'):
  os.makedirs(output_dir, exist_ok=True)
  fig, ax = plt.subplots(figsize=(7, 4.5))

  sns.lineplot(
      data=df,
      x='batch_size',
      y='latency_ms',
      hue='model_type',
      style='model_type',
      markers=True,
      dashes=True,
      linewidth=2,
      markersize=7,
      errorbar=('ci', 95),
      ax=ax,
  )

  ax.set_xlabel('Batch Load (Sample Count [items])', fontweight='bold')
  ax.set_ylabel('Inference Latency (ms)', fontweight='bold')
  ax.set_title(
      'Figure 1: Benchmark Latency vs. Batch Load (95% CI)',
      fontweight='bold',
      pad=12,
  )
  ax.grid(True, linestyle='--', alpha=0.5)

  handles, labels = ax.get_legend_handles_labels()
  ax.legend(
      handles=handles,
      labels=['Baseline (Rule-Based)', 'Proposed AI Classifier'],
      title='Method',
  )

  fig.savefig(
      f'{output_dir}/fig1_latency_vs_load.pdf',
      format='pdf',
      bbox_inches='tight',
  )
  fig.savefig(
      f'{output_dir}/fig1_latency_vs_load.png',
      format='png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.close(fig)


def plot_distribution_boxplot(
    df: pd.DataFrame, output_dir: str = 'reports/figures'
):
  os.makedirs(output_dir, exist_ok=True)
  fig, ax = plt.subplots(figsize=(6, 4.5))

  df_plot = df.copy()
  df_plot['accuracy_pct'] = df_plot['accuracy'] * 100.0

  palette = sns.color_palette('colorblind')

  sns.boxplot(
      data=df_plot,
      x='model_type',
      y='accuracy_pct',
      palette=[palette[0], palette[2]],
      width=0.4,
      boxprops=dict(alpha=0.7),
      ax=ax,
  )

  sns.stripplot(
      data=df_plot,
      x='model_type',
      y='accuracy_pct',
      color='black',
      alpha=0.5,
      jitter=0.15,
      size=5,
      ax=ax,
  )

  ax.set_xticklabels(['Baseline (Rule-Based)', 'Proposed AI Classifier'])
  ax.set_xlabel('Phishing Classification Method', fontweight='bold')
  ax.set_ylabel('Detection Accuracy (%)', fontweight='bold')
  ax.set_title(
      'Figure 2: Empirical Accuracy Distribution', fontweight='bold', pad=12
  )
  ax.grid(True, linestyle='--', alpha=0.5, axis='y')

  fig.savefig(
      f'{output_dir}/fig2_distribution_boxplot.pdf',
      format='pdf',
      bbox_inches='tight',
  )
  fig.savefig(
      f'{output_dir}/fig2_distribution_boxplot.png',
      format='png',
      dpi=300,
      bbox_inches='tight',
  )
  plt.close(fig)


if __name__ == '__main__':
  import os
  from process_data import filter_warmup, load_raw_data

  data_path = (
      'data/raw/test_run.jsonl'
      if os.path.exists('data/raw/test_run.jsonl')
      else '../data/raw/test_run.jsonl'
  )
  output_dir = (
      'reports/figures'
      if os.path.exists('reports')
      else '../reports/figures'
  )

  raw_df = load_raw_data(data_path)
  eval_df = filter_warmup(raw_df)
  plot_latency_vs_load(eval_df, output_dir=output_dir)
  plot_distribution_boxplot(eval_df, output_dir=output_dir)
  print(f'All figures successfully exported to {output_dir}')