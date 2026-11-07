import json
import os
import yaml


def load_config(config_path="config.yaml"):
    """Загрузка конфигурационного файла."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    # 1. Читаем конфигурацию
    config = load_config()
    print("[INFO] Конфигурация config.yaml успешно загружена.")

    # 2. Итоговые метрики вашего исследования (из Паспорта исследования)
    metrics = {
        "primary_metric": {"detection_accuracy_pct": 94.2},
        "secondary_metrics": {
            "error_rate_per_100_words": 1.15,
            "flesch_kincaid_index": 68.4,
            "trust_rating_likert": 5.4,
            "action_execution_rate_pct": 12.8,
        },
        "guardrail_metrics": {
            "execution_latency_ms": 1340,
            "false_positive_rate_pct": 3.1,
            "unhandled_exceptions": 0,
        },
    }

    # 3. Путь для сохранения итогов (берем из config.yaml)
    output_path = config["output"]["metrics_path"]

    # Создаем папку results, если её ещё нет
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 4. Сохраняем метрики в JSON-файл
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=4, ensure_ascii=False)

    print(f"[SUCCESS] Результаты сохранены в файл: {output_path}")


if __name__ == "__main__":
    main()