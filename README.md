# Asset-Agnostic Historical Simulation Framework

A modular, high-performance backtesting engine engineered in Python to ingest multi-year data streams, eliminate data leakage, and execute full performance attribution. 

The core objective of this codebase is not to present an optimized alpha strategy, but to build a robust testing laboratory capable of exposing structural flaws and risk profiles before live capital allocation.

---

## 🛠️ System Architecture & Safeguards

To maintain absolute analytical integrity, the engine incorporates specific production-grade engineering principles:

* **Vectorized Processing Environment:** Leverages Pandas matrix operations to compute portfolio metrics across the entire historical horizon simultaneously, completely bypassing slow, performance-heavy iterative loops (`for` loops).
* **Look-Ahead Bias Mitigation:** Implements a strict chronological execution lag on alpha signals (row-shifting triggers) to ensure the framework never accidentally "peeks" into tomorrow's data to make today's trade.
* **Automated Risk Mapping:** Programmed with continuous peak-tracking arithmetic to dynamically map real-time portfolio drawdown exposure across fluctuating market regimes.

---

## 📊 Empirical Verification Run (Case Study)

To stress-test the pipeline, a mechanical trend-following indicator was deployed as a verification strategy. The framework backtested the model over a **10-year historical horizon** against a mega-cap, high-momentum asset baseline (**AAPL**).

### Execution Terminal Outputs:

| Metric | Benchmark (Buy & Hold) | Systematic Trend Strategy |
| :--- | :---: | :---: |
| **Cumulative Return** | ~13.29x | ~3.51x |
| **Maximum Drawdown** | -31.4% | -13.8% |

### Quantitative Performance Diagnosis:
The simulation exposed a clear structural trade-off. The verification strategy experienced severe absolute underperformance due to the inherent mathematical latency of trailing indicators within a powerful secular bull market. Because the equity regime was characterized by rapid, V-shaped recoveries, trailing lag created significant upside execution drag. 

However, looking strictly at risk-adjusted metrics, the software successfully validated the model's capacity to function as an asymmetric capital shield—compressing systemic peak-to-trough drawdown exposure by **56%**.

---

## 💻 Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Libraries:** `pandas`, `yfinance`
* **Design Pattern:** Object-Oriented Programming (OOP)

---

## 📂 Repository Structure

* `Project 1- Algorithmic BackTester.py` - Core execution engine containing data-ingestion, signaling logic, and portfolio tracking modules.
* `README.md` - Framework documentation and analytical case study.
