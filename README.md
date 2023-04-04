# Loan-Approval-prediction [App](https://sukriti2812-loan-approval-prediction-app-9ulbbe.streamlit.app/)

## Overview
This project is aimed at predicting the likelihood of a loan applicant defaulting based on various features such as income, credit history, loan amount, etc. The dataset used for this project is sourced from Kaggle and consists of 614 observations with 13 features.

## Data Preprocessing
The dataset required extensive cleaning and preprocessing before it could be used for building models. This included handling missing values, encoding categorical variables, scaling numerical features, and handling outliers.

## Feature Engineering
Several new features were derived from the existing features to improve the model performance.
For instance, the total income of the applicant and co-applicant was computed, some new feature were created to indicate the loan repayment capacity like EMI, Balance Income, etc.

## Model Building
Several machine learning algorithms were evaluated for their performance in predicting loan defaults. These included logistic regression, decision tree, random forest, and XGBoost algorithms.
The best performing model was Random Forest based on its accuracy and interpretability.

## Model Deployment
The final model was deployed as a web application using Streamlit. The user can input the necessary details, and the model would predict the likelihood of the loan approval.

# Conclusion
The loan prediction model developed in this project has an accuracy of 80% in predicting loan approvals. The model can be used by banks and financial institutions to assess the creditworthiness of loan applicants and make informed lending decisions.
