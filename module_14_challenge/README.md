# Module 14 Challenge

![14-4-challenge-image](https://user-images.githubusercontent.com/25112189/180666655-298fc44a-2133-407f-bbd2-fa058ea8e6f8.png)

---

## Background

In this Challenge, we assume the role of a financial advisor at one of the top five financial advisory firms in the world. Our firm constantly competes with the other major firms to manage and automatically trade assets in a highly dynamic environment. In recent years, the firm has heavily profited by using computer algorithms that can buy and sell faster than human trader.  
  
The speed of these transactions gave our firm a competitive advantage early on, but people still need to specifically program these systems, which limits their ability to adapt to new data. We're planning to improve the existing algorithmic trading systems and maintain the firm’s competitive advantage in the market. To do so, we’ll enhance the existing trading signals with machine learning algorithms that can adapt to new data.

---

## Tuning Results

### Tuned Model
![tuned_model](https://user-images.githubusercontent.com/25112189/180668009-de6d72e7-aec6-4e53-873d-63576b8fad08.png)

### AdaBoost Model
![AdaBoost_model](https://user-images.githubusercontent.com/25112189/180668265-7e894de5-79f3-411c-8045-5d30661a18e3.png)

### Responses
1. What impact resulted from increasing or decreasing the training window?
  - By increasing the training window from three months to six months, we reveal a long-term increase in strategy returns.
2. What impact resulted from increasing or decreasing either or both of the SMA windows?
  - Increasing the short window from four to 20 did not result in major changes.
  - Decreasing the long window from 100 to 50 had significant negative results and our returns were much lower.
3. Did this new model perform better or worse than the provided baseline model?
  - A tuned model performed better than the provided baseline model.  The AdaBoost model 
4. Did this new model perform better or worse than your tuned trading algorithm?
  - The AdaBoost Model performed remarkably similar to the tuned model. 
  - Recall for 1 was better on the tuned model while recall for -1 was better on the AdaBoost model.
  - The tuned model had a higher f1 score.

---

## Installation

```sh
git clone git@github.com:travispeska/gwu_fintech.git
cd gwu_fintech/module_14_challenge/
pip install -r requirements.txt
```

---

## Jupyter Notebook Usage

```sh
jupyter lab
Open Browser > http://localhost:8888/lab/tree/machine_learning_trading_bot.ipynb
```

---

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
