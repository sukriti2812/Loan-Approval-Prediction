import streamlit as st
import pandas as pd
import joblib

# Load the trained model and any necessary data files
model = joblib.load('loan_approval_model.pkl')
data = pd.read_csv('loan_applications.csv')

# Define the Streamlit app
def app():
    # Create a form for the user to input loan applicant information
    st.header('Loan Approval Prediction')
    st.subheader('Enter loan applicant information')
    loan_amount = st.number_input('Loan Amount')
    term = st.number_input('Loan Term (in months)')
    credit_score = st.number_input('Credit Score')
    income = st.number_input('Annual Income')

    # Make a prediction based on the user input
    prediction = model.predict([[loan_amount, term, credit_score, income]])
    if prediction[0] == 1:
        result = 'approved'
    else:
        result = 'denied'

    # Output the prediction result to the user
    st.subheader('Loan approval prediction:')
    st.write('The loan application is likely to be', result)

# Run the Streamlit app
if __name__ == '__main__':
    app()