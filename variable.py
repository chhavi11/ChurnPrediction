from pydantic import BaseModel

class variable(BaseModel):
    tenure:float                                
    MonthlyCharges:float                           
    TotalCharges :float                            
    Contract_One_year:int                          
    Contract_Two_year:int                          
    Dependents_Yes :int                            
    DeviceProtection_No_internet_service:int       
    DeviceProtection_Yes:int                       
    gender_Male :int                              
    InternetService_Fiber_optic :int               
    InternetService_No :int                        
    MultipleLines_No_phone_service :int            
    MultipleLines_Yes:int                          
    OnlineBackup_No_internet_service:int           
    OnlineBackup_Yes :int                          
    OnlineSecurity_No_internet_service :int        
    OnlineSecurity_Yes:int                         
    PaperlessBilling_Yes :int                      
    Partner_Yes :int                               
    PaymentMethod_Credit_card:int      
    PaymentMethod_Electronic_check :int            
    PaymentMethod_Mailed_check :int                 
    PhoneService_Yes :int                           
    SeniorCitizen_1 :int                            
    StreamingMovies_No_internet_service :int        
    StreamingMovies_Yes  :int                      
    StreamingTV_No_internet_service :int            
    StreamingTV_Yes :int                            
    TechSupport_No_internet_service :int            
    TechSupport_Yes :int                                                                 