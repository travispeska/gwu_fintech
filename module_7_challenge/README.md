# Module 7 Challenge

![7-4-challenge-image](https://user-images.githubusercontent.com/25112189/171067443-abda6b6d-a9a6-4585-bcaf-e492cb2c6039.png)

---

## Background
In recent years, finance has had an explosion in passive investing. Passive investing means that you invest in a basket of assets that’s called an exchange-traded fund (ETF). This way, you don’t spend time researching individual stocks or companies or take the risk of investing in a single stock. ETFs offer more diversification.

In this Challenge assignment, we build a financial database and web application by using SQL, Python, and the Voilà library to analyze the performance of a hypothetical fintech ETF.

---

## Purpose
Using the provided `etf.db` SQLite Database, this notebook conducts analysis of the GDOT, GS, PYPL, and SQ tickers.

This module is broken down into four parts:
1. Analysis of a single asset in the ETF
2. Optimatization of data access with advanced SQL queries
3. Analysis of the ETF portfolio
4. Deployment of the notebook as a web application with viola

---

## Installation

```sh
git clone git@github.com:travispeska/gwu_fintech.git
cd gwu_fintech/module_7_challenge/
pip install -r requirements.txt
```

---

## Jupyter Notebook Usage

```sh
jupyter lab
Open Browser > http://localhost:8888/lab/tree/etf_analyzer.ipynb
```

---

## Web Application Deployment

```sh
voila etf_analyzer.ipynb
Open Browser > http://localhost:8866/
```

![image](https://user-images.githubusercontent.com/25112189/171069115-2be1c5ad-7e27-4362-aec8-d255abc18db5.png)
[Full Viola Demonstration](https://user-images.githubusercontent.com/25112189/171069083-a4b2c0b0-7e13-45c9-a3fe-4457c232ba75.mp4)

---

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
