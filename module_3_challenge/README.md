# Module 3 Challenge

---

## Crypto Arbitrage

This Jupyter Notebook is used to analyze historical trade date from the Bitstamp and Coinbase Bitcoin exchanges.  It does this by ingesting two CSV files from ./Resources/ .  

All three phases of financial analysis are undertaken in order to answer some final analytical questions. 

The three phases include:
1. Collection of the data
2. Preparation of the data
3. Analysis of the data

### Crypto Arbitrage Analysis

The notebook performs analysis of the cost of Bitcoin on specific days.  Three dates are chosen toward the beginning, middle, and end of the datasets.  The notebook identifies opportunities to for arbritage exploitation by identifying the cost of Bitcoin on both exchanges specific dates and times. The sum of possible arbitrage profits is identified and used to determine a shrinking degree of spread over time.

---

## Installation

```sh
git clone git@github.com:travispeska/gwu_fintech.git
cd gwu_fintech/module_3_challenge/
pip install -r requirements.txt
```

---

## Usage

```sh
jupyter lab
Open Browser > http://localhost:8889/lab/tree/crypto_arbitrage.ipynb
```

---

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
