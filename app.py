import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

# loading the trained model
classifier = pickle.load(open('loan_approval_model.pkl', 'rb'))
 
@st.cache_data()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, Dependents, Education, Self_Employed, Credit_History, Property_Area, LoanAmount, LoanAmount_term, ApplicantIncome, CoapplicantIncome):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
    
    if Dependents == "0":
        Dependents = 0    
    elif Dependents == "1":
        Dependents = 1
    elif Dependents == "2":
        Dependents = 2
    elif Dependents == "3+":
        Dependents = 3

    if Education == "Graduate":
        Education = 1
    else:
        Education = 0

    if Self_Employed == "Yes":
        Self_Employed = 1
    else:
        Self_Employed = 0

    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
    
    if Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semi-urban":
        Property_Area = 1
    else:
        Property_Area = 2
    
    LoanAmount_log = np.log(LoanAmount)
    Total_Income = ApplicantIncome + CoapplicantIncome
    Total_Income_log = np.log(Total_Income)
    EMI = LoanAmount / LoanAmount_term
    Balance_Income = Total_Income - (EMI*1000)
 
    # Making predictions 
    prediction = classifier.predict(
        [[Gender, Married, Dependents, Education, Self_Employed, Credit_History, Property_Area, LoanAmount_log, Total_Income, Total_Income_log, EMI, Balance_Income]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def app():       
    # front end elements of the web page 
    html_temp = """
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Loan Prediction Web App</h1> 
    </div> 
    """
    
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction
    sel_col, disp_col = st.columns(2)

    Gender = sel_col.selectbox("Gender",("Male","Female"))
    Married = sel_col.selectbox('Marital Status',("Unmarried","Married"))
    Dependents = sel_col.selectbox('Dependents',("0","1","2","3+"))
    Education = sel_col.selectbox('Educational Qualifications',("Graduate","Not Graduate"))
    Self_Employed = sel_col.selectbox('Self Employed',("Yes","No"))
    Credit_History = disp_col.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    Property_Area = disp_col.selectbox('Property Area',("Rural","Semi-urban","Urban"))
    LoanAmount = disp_col.number_input("Total loan amount (in thousands)")
    LoanAmount_term = disp_col.number_input("Loan Amount term (in months)")
    ApplicantIncome = disp_col.number_input("Applicant Income")
    CoapplicantIncome = sel_col.number_input("Coapplicant Income")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, Credit_History, Property_Area, LoanAmount, LoanAmount_term, ApplicantIncome, CoapplicantIncome) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    app()
