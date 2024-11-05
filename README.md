# Customer Churn Prediction
## Problem
A small-sized startup is keen on reducing its customer churn and has hired you as a Machine Learning engineer for this task. Churn rate is a marketing metric that describes the number of customers who leave a business over a specific time period. Every user is assigned a prediction value that estimates their state of churn at any given time. This value is based on:
- User demographic information
- Browsing behavior
- Historical purchase data among other information

## Task
As an expert, you are required to build a sophisticated Machine Learning model that predicts the churn score for a website based on multiple features.

## Data description
The dataset folder contains the following files:
- train.csv: 36992 x 25
- test.csv: 19919 x 24

The columns provided in the dataset are as follows:

| Column Name                   | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| customer_id                   | Represents the unique identification number of a customer                   |
| Name                          | Represents the name of a customer                                           |
| age                           | Represents the age of a customer                                            |
| security_no                   | Represents a unique security number that is used to identify a person       |
| region_category               | Represents the region that a customer belongs to                            |
| membership_category           | Represents the category of the membership that a customer is using          |
| joining_date                  | Represents the date when a customer became a member                         |
| joined_through_referral       | Represents whether a customer joined using any referral code or ID          |
| referral_id                   | Represents a referral ID                                                    |
| preferred_offer_types         | Represents the type of offer that a customer prefers                        |
| medium_of_operation           | Represents the medium of operation that a customer uses for transactions    |
| internet_option               | Represents the type of internet service a customer uses                     |
| last_visit_time               | Represents the last time a customer visited the website                     |
| days_since_last_login         | Represents the no. of days since a customer last logged into the website     |
| avg_time_spent                | Represents the average time spent by a customer on the website              |
| avg_transaction_value         | Represents the average transaction value of a customer                      |
| avg_frequency_login_days      | Represents the no. of times a customer has logged in to the website          |
| points_in_wallet              | Represents the points awarded to a customer on each transaction             |
| used_special_discount         | Represents whether a customer uses special discounts offered                |
| offer_application_preference  | Represents whether a customer prefers offers                                |
| past_complaint                | Represents whether a customer has raised any complaints                     |
| complaint_status              | Represents whether the complaints raised by a customer were resolved        |
| feedback                      | Represents the feedback provided by a customer                              |
| churn_risk_score              | Represents the churn risk score that ranges from 1 to 5                     |


[Source](https://www.hackerearth.com/problem/machine-learning/predict-the-churn-risk-rate-11-fb7a760d/)

## Analysis
[See the document for the analysis done](https://github.com/aayomide/churn-risk-prediction/blob/main/customer%20churn%20prediction.ipynb)

## Web App
The predictive model built in this project was deployed to a web app developed using Python/Flask for the backend and HTML/CSS/Bootstrap for the front end. 
[Live site](https://churn-risk-prediction-1.onrender.com/)

### Built with 
- Front-end: HTML/CSS, Bootstrap
- Backend: Python/Flask
- Deployment: Render
- Machine Learning Algorithm: XGBoost classifier


----
## Setup
For this project, having a Python version less than v3.12 on your system is preferable to avoid compatibility issues during dependencies installation. Python 3.10.11 was used in the project. <br>
Check your Python version by inputting `python --version` in the command-line prompt.

Follow these steps to set up the development environment for the churn prediction project:
1. Create a Project Directory:
    - Open your terminal and create a new directory on your local machine called churn_prediction: `mkdir churn_prediction`
2. Navigate to this new Project Directory: `cd churn_prediction`
3. Create a Python virtual environment inside the churn_prediction directory: `python -m venv .venv`
4. Activate the Virtual Environment: `.venv\Scripts\activate`
5. While still in the churn_prediction directory, clone this project repository into your local: `git clone https://github.com/aayomide/churn-risk-prediction.git`
6. Navigate to the Cloned Repository: `cd churn-risk-prediction`
7. Install all required dependencies using pip: `pip install -r requirements.txt`
8. Start the Web Application. Run the following command to start the Flask web application: `flask run`
