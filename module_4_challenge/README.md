# Module 4 Challenge

---

## Risk Return Analysis

This Jupyter Notebook is used to analyze the potential risk of four investment funds based on historical data associated with each.  It does this by ingesting a CSV file called ./Resources/whale_navs.csv.  

For each of the four funds we determine:
1. Daily Returns
2. Standard Deviations
3. Sharpe Ratios
4. Beta Values

### Visualizations

This notebook builds visualizations of the daily returns, cumulative returns, and standard deviations for each of the funds alongside the S&P 500.  The two funds with the highest Sharpe values are then compared by plotting their Beta values across a 60 day rolling window.

---

## Installation

```sh
git clone git@github.com:travispeska/gwu_fintech.git
cd gwu_fintech/module_4_challenge/
pip install -r requirements.txt
```

---

## Usage

```sh
jupyter lab
Open Browser > http://localhost:8889/lab/tree/risk_return_analysis.ipynb
```

---

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
