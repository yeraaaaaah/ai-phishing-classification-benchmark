# Classification of Textual AI-Phishing Methods in Personal Communications of Private Users

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Docker Support](https://img.shields.io/badge/Docker-Ready-green.svg)](https://www.docker.com/)

---

## 📌 Research Overview

The rapid advancement of Large Language Models (LLMs) and generative artificial intelligence has fundamentally redefined social engineering vectors. Traditional textual phishing relied heavily on unpersonalized mass distribution, noticeable syntactical errors, and crude formatting. Modern AI-enabled threats (**Phishing 2.0**) leverage LLMs to produce contextually tailored, grammatically flawless, and hyper-formal deceptive messages at scale.

This repository implements a lightweight benchmark pipeline and reproducible methodology framework to evaluate structural-linguistic characteristics and spontaneous user vigilance against AI-generated phishing texts in personal communication channels (email, instant messaging, and social networks).

---

## 👥 Authors & Academic Context

* **Authors:** Tursynbayev Yerassyl, Ospankul Zharkyn
* **Course Assignment:** Task 2 — Methodology Passport Card & Research Repository
* **Project Status:** Active Development (W5–W6 Benchmark Execution Phase)

---

## ❓ Research Questions

* **RQ1 (Exploratory / Descriptive):** What key structural-linguistic characteristics, categories, and patterns predominate in AI-generated phishing messages during attacks on private users via instant messengers and email?
* **RQ2 (Explanatory):** How does the deployment of large language models (LLMs) alter psychological influence mechanisms in phishing texts compared to traditional ("manual") phishing, and why does this reduce users' spontaneous vigilance?

---

## 🔬 Hypotheses Summary

* **H1.1:** AI-generated phishing messages exhibit statistically higher linguistic coherence and fewer grammatical/syntactical errors compared to traditional ("manual") phishing texts.
* **H1.2:** In AI-generated phishing texts, adherence to formal tone-of-voice and domain-specific terminology predominates over aggressive emotional calls-to-action.
* **H2.1:** Users' level of spontaneous vigilance when evaluating AI-generated phishing messages is statistically lower than when evaluating traditional manual phishing messages.
* **H2.2:** The absence of overt linguistic anomalies ("red flags") in AI-phishing enhances the psychological trigger of "sender authority," increasing users' willingness to execute target actions.

---

## 📂 Repository Structure

```text
.
├── configs/
│   └── config.yaml               # Experimental parameters and dataset configuration
├── data/
│   └── sample/
│       └── phishing_samples.json # Test sample dataset for pipeline validation
├── src/
│   └── benchmark.py              # Executable benchmark python script
├── .gitignore                    # Git cache and technical file exclusions
├── Dockerfile                    # Containerization configuration
├── LICENSE                       # MIT Open Source License
└── README.md                     # Academic overview and quickstart guide
```

---

## 🚀 Planned Benchmarks & Metrics Matrix

| Metric Category | Target Indicator | Baseline Comparison | Guardrail Threshold |
| :--- | :--- | :--- | :--- |
| **Linguistic Quality** | Error count per 100 words & Flesch-Kincaid Index | Traditional Manual Phishing Corpus | N/A |
| **Stylistic Pattern** | Ratio of Formal Tone vs. Urgent Emotional Markers | Standard Security Threat Reports | N/A |
| **Detection Performance** | Spontaneous Detection Accuracy (%) | Baseline Rule-based Classifiers | False Positive Rate < 5% |
| **Pipeline Latency** | Benchmark Execution Time (ms) | Legacy Processing Script | Latency < 2000 ms per text sample |

---

## ⚡ Quickstart Guide

### Option 1: Native Python Execution

1. Run the benchmark pipeline on sample data:
   ```bash
   python src/benchmark.py
   ```

### Option 2: Docker Execution

1. Build the Docker image:
   ```bash
   docker build -t ai-phishing-benchmark .
   ```

2. Execute the containerized benchmark:
   ```bash
   docker run --rm ai-phishing-benchmark
   ```

---

## 📄 License

This project is licensed under the MIT License.
