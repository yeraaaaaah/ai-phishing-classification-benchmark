# Mathematical Domain Model & Loss Function Formalization

**Research Title:** Classification of Textual AI-Phishing Methods in Personal Communications of Private Users  
**Authors:** Tursynbayev Yerassyl, Ospankul Zharkyn  
**Track:** Machine Learning / Artificial Intelligence (ML/AI)

---

## 1. Problem Formulation & Objective Function

Let $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}$ denote the benchmark dataset of textual communication samples, where:
- $x_i \in \mathcal{X}$ represents the textual sequence of sample $i$.
- $y_i \in \{0, 1\}$ is the ground-truth target label, where $y_i = 1$ indicates an AI-generated phishing message, and $y_i = 0$ indicates a legitimate message.

The proposed classifier parameterized by $\theta$ predicts the probability $\hat{y}_i = P(y_i = 1 \mid x_i; \theta)$.

### Loss Function ($\mathcal{L}$)
To handle dataset imbalance and penalize confident misclassifications, we optimize a **Focal-Regularized Binary Cross-Entropy Loss** defined as:

$$\mathcal{L}(\theta) = - \frac{1}{N} \sum_{i=1}^{N} \left[ \alpha y_i (1 - \hat{y}_i)^\gamma \log(\hat{y}_i) + (1 - \alpha)(1 - y_i) \hat{y}_i^\gamma \log(1 - \hat{y}_i) \right] + \lambda \|\theta\|_2^2$$

Where:
- $\alpha \in (0, 1)$ is the class imbalance weighting factor ($\alpha = 0.75$).
- $\gamma \ge 0$ is the focal focusing parameter modulating down-weighting of easy examples ($\gamma = 2.0$).
- $\lambda \|\theta\|_2^2$ is the $L_2$ weight regularization penalty ($\lambda = 10^{-4}$).

---

## 2. Target Metrics Formalization

### A. Primary Operational Metric: Human Detection Accuracy ($\text{Acc}$)
$$\text{Acc} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \times 100\%$$

### B. Guardrail Metric 1: False Positive Rate ($\text{FPR}$)
$$\text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}} \le 0.05 \quad (5\%)$$

### C. Guardrail Metric 2: Latency Percentile ($L_{p95}$)
$$L_{p95} = \inf \left\{ l \in \mathbb{R} \mid P(L_i \le l) \ge 0.95 \right\} < 2000\text{ ms}$$

### D. Non-Parametric 95% Bootstrap Confidence Interval
For metric estimate $\hat{\mu}$, the $95\%$ bootstrap confidence interval is computed over $B = 1000$ resamples:

$$\text{CI}_{95\%} = \left[ Q\left(\frac{\alpha_{ci}}{2}\right), Q\left(1 - \frac{\alpha_{ci}}{2}\right) \right]$$

where $Q(q)$ is the $q$-th percentile of empirical bootstrap distribution $\{\hat{\mu}^{*b}\}_{b=1}^{B}$ with fixed random seed $S = 42$.

---

## 3. Mathematical Notation Table

| Notation | Entity Description | Dimension / Type |
| :--- | :--- | :--- |
| $\mathcal{X}$ | Input text sequence space | Character / Token Sequence |
| $y_i \in \{0, 1\}$ | Binary phishing target label | Discrete $\{0, 1\}$ |
| $\hat{y}_i \in [0, 1]$ | Predicted model probability | Continuous Scalar |
| $\theta$ | Model parameters / weights | $\mathbb{R}^d$ Vector |
| $\alpha$ | Imbalance factor | Scalar $(\alpha = 0.75)$ |
| $\gamma$ | Focal parameter | Scalar $(\gamma = 2.0)$ |
| $\lambda$ | Weight decay hyperparameter | Scalar $(\lambda = 10^{-4})$ |
| $L_{p95}$ | 95th Percentile Latency | Milliseconds (ms) |
| $\text{FPR}$ | False Positive Rate | Percentage $(\%)$ |