# Module 12 Report

## Overview of the Analysis

In this challenge I analyzed loans and made predictions about the status of additional loans.  Beginning with 75036 data points of healthy loans and 2500 data points of high-risk loans, I created a logistic regression model to make predictions about the data sets.  Because the sample size for high-risk loans was significantly smaller than the healthy loan sample size, I had to increase the size of the minority by using a random oversampler model.

## Results

* Machine Learning Model 1:
  * Original data contained 75036 healthy loan data points and 2500 high risk loan data points
  * Healthy Loan Precision: 100%
  * Healthy Loan Recall: 99%
  * Healthy Loan f1 Score: 100%
  * High-Risk Loan Precision: 85%
  * High-Risk Loan Recall: 91%
  * High-Risk Loan f1 Score: 88%
  * Balanced Accuracy Score: 95%


* Machine Learning Model 2:
  * This oversampled dataset used 56271 healthy loan data points and 56271 high-risk loan data points
  * Healthy Loan Precision: 100%
  * Healthy Loan Recall: 99%
  * Healthy Loan f1 Score: 100%
  * High-Risk Loan Precision: 84%
  * High-Risk Loan Recall: 99%
  * High-Risk Loan f1 Score: 91%
  * Balanced Accuracy Score: 99%

## Summary

Because the original dataset was so healvily imbalanced, I had to use random oversampling in order to build a better balanced dataset.  This model proved successful and is providing accurate and beneficial results.
