
# README: Crop Production Prediction AI Project

---

## Project Overview

This project is an **AI-based Crop Production Prediction system** that estimates the amount of crop yield per acre of land. It uses historical and current data from over **101 countries** to predict crop production based on key environmental and agricultural factors.

---

## Problem Statement

Farmers and agricultural planners often lack accurate tools to estimate crop yields in advance, which leads to inefficient use of resources like pesticides, water, and land. This project aims to provide reliable predictions to help in better planning and decision-making.

---

## Data and Features

The model uses the following input parameters:

* **Country**: Location of the crop production
* **Crop Type**: One of 10 different crops (e.g., wheat, rice, maize)
* **Average Rainfall**: Rainfall during the crop season
* **Average Temperature**: Temperature during the crop season
* **Total Pesticides Used**: Amount of pesticides used across the crop area

---

## Solution Approach

* The model is built using **Machine Learning**, specifically the **Stochastic Gradient Descent (SGD) Regressor** algorithm, implemented in Python with scikit-learn.
* To improve model performance, **Polynomial Features** (degree 2) were added, allowing the model to capture complex relationships between variables.
* The model was trained and validated on a large dataset spanning 101 countries.

---

## Performance

* **Before polynomial features:**

  * Training accuracy: \~78%
  * Testing accuracy: \~75%
* **After adding polynomial features:**

  * Training accuracy: \~94%
  * Testing accuracy: \~95%

---

## Real-World Testing

The model was tested with real data from Australia (2024 wheat production):

* Actual production: \~15 quintals per acre
* Model prediction: 13.4 quintals per acre

This shows the model's predictions closely match real-world values.

---

## Benefits and Future Use

* Helps farmers understand how changes in temperature, rainfall, or pesticide use affect crop yield.
* Supports better decision-making about which crops to plant and how to manage resources.
* Can be used by agricultural planners and government bodies for food supply forecasting.

---

## Technical Details

* Language: Python
* Libraries: scikit-learn, pandas, numpy, Streamlit (for UI)
* Model: SGD Regressor with polynomial features
* Dataset: Crop production data from 101 countries

---

## How to Use

A simple Streamlit web app was developed to allow users to input parameters and get crop yield predictions instantly.

Link to app: [https://crop-predict-pawan.streamlit.app/](https://crop-predict-pawan.streamlit.app/)

---

## Contact

* Name: Pawan Yadav
* Email: [yaduvanshi2000pawan@gmail.com](mailto:yaduvanshi2000pawan@gmail.com)

---

*Thank you for reviewing my project!*

---

