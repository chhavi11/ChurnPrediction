import streamlit
import requests
import json
        
def run():
    streamlit.title("Churn Prediction")
    streamlit.title("Please enter the data in Numeric form")
    tenure = streamlit.number_input("tenure")
    MonthlyCharges = streamlit.number_input("MonthlyCharges")
    TotalCharges = streamlit.number_input("TotalCharges")
    streamlit.title("From Here Please enter the data in the form of 0 and 1")
    Contract_One_year = streamlit.number_input("Contract_One_year",0,1)
    Contract_Two_year = streamlit.number_input("Contract_Two_year",0,1)
    Dependents_Yes = streamlit.number_input("Dependents_Yes",0,1)
    DeviceProtection_No_internet_service = streamlit.number_input("DeviceProtection_No_internet_service",0,1)
    DeviceProtection_Yes = streamlit.number_input("DeviceProtection_Yes",0,1)
    gender_Male = streamlit.number_input("gender_Male",0,1)
    InternetService_Fiber_optic  = streamlit.number_input("InternetService_Fiber_optic",0,1)
    InternetService_No = streamlit.number_input("InternetService_No",0,1)
    MultipleLines_No_phone_service =streamlit.number_input('MultipleLines_No_phone_service',0,1)        
    MultipleLines_Yes=streamlit.number_input('MultipleLines_Yes',0,1)                        
    OnlineBackup_No_internet_service=streamlit.number_input('OnlineBackup_No_internet_service',0,1)     
    OnlineBackup_Yes =streamlit.number_input('OnlineBackup_Yes',0,1)                        
    OnlineSecurity_No_internet_service =streamlit.number_input('OnlineSecurity_No_internet_service',0,1)        
    OnlineSecurity_Yes=streamlit.number_input('OnlineSecurity_Yes',0,1)     
    PaperlessBilling_Yes =streamlit.number_input('PaperlessBilling_Yes',0,1)   
    Partner_Yes =streamlit.number_input('Partner_Yes',0,1)                               
    PaymentMethod_Credit_card=streamlit.number_input('PaymentMethod_Credit_card',0,1)      
    PaymentMethod_Electronic_check =streamlit.number_input('PaymentMethod_Electronic_check',0,1)            
    PaymentMethod_Mailed_check =streamlit.number_input('PaymentMethod_Mailed_check',0,1)                 
    PhoneService_Yes =streamlit.number_input('PhoneService_Yes',0,1)            
    SeniorCitizen_1 =streamlit.number_input('SeniorCitizen_1',0,1)                     
    StreamingMovies_No_internet_service =streamlit.number_input('StreamingMovies_No_internet_service',0,1)        
    StreamingMovies_Yes  =streamlit.number_input('StreamingMovies_Yes',0,1)                      
    StreamingTV_No_internet_service =streamlit.number_input('StreamingTV_No_internet_service',0,1)            
    StreamingTV_Yes =streamlit.number_input('StreamingTV_Yes',0,1)                            
    TechSupport_No_internet_service =streamlit.number_input('TechSupport_No_internet_service',0,1)            
    TechSupport_Yes =streamlit.number_input('TechSupport_Yes',0,1) 
    
    
    data = { 
    'tenure':tenure,                                
    'MonthlyCharges': MonthlyCharges ,                          
    'TotalCharges' :TotalCharges ,                           
    'Contract_One_year':Contract_One_year ,                         
    'Contract_Two_year':Contract_Two_year,                          
    'Dependents_Yes' :Dependents_Yes ,                           
    'DeviceProtection_No_internet_service':DeviceProtection_No_internet_service ,      
    'DeviceProtection_Yes':DeviceProtection_Yes ,                      
    'gender_Male' :gender_Male ,                             
    'InternetService_Fiber_optic' :InternetService_Fiber_optic ,              
    'InternetService_No' :InternetService_No,                        
    'MultipleLines_No_phone_service' :MultipleLines_No_phone_service,            
    'MultipleLines_Yes':MultipleLines_Yes,                          
    'OnlineBackup_No_internet_service':OnlineBackup_No_internet_service,           
    'OnlineBackup_Yes' :OnlineBackup_Yes,                          
    'OnlineSecurity_No_internet_service' :OnlineSecurity_No_internet_service,        
    'OnlineSecurity_Yes':OnlineSecurity_Yes,                         
    'PaperlessBilling_Yes' :PaperlessBilling_Yes,                      
    'Partner_Yes' :Partner_Yes,                               
    'PaymentMethod_Credit_card':PaymentMethod_Credit_card,      
    'PaymentMethod_Electronic_check' :PaymentMethod_Electronic_check,            
    'PaymentMethod_Mailed_check' :PaymentMethod_Mailed_check,                 
    'PhoneService_Yes' :PhoneService_Yes,                           
    'SeniorCitizen_1' :SeniorCitizen_1,                            
    'StreamingMovies_No_internet_service' :StreamingMovies_No_internet_service,        
    'StreamingMovies_Yes'  :StreamingMovies_Yes,                      
    'StreamingTV_No_internet_service' :StreamingTV_No_internet_service,            
    'StreamingTV_Yes' :StreamingTV_Yes,                            
    'TechSupport_No_internet_service' :TechSupport_No_internet_service,            
    'TechSupport_Yes' :TechSupport_Yes 
    }
    
    if streamlit.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        prediction =response.text
        print(prediction)
        streamlit.success(f"The prediction from model: {prediction}")
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()
