import uvicorn
from fastapi import FastAPI
from variable import variable
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("LogReg_pickle2","rb")
model=pickle.load(pickle_in)

scale = open("scaler","rb")
scal=pickle.load(scale)

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Churn Prediction Model': f'{name}'}


@app.post('/predict')
def churnPrediction(data:variable):
    data_dict = data.dict()
    data_df = pd.DataFrame.from_dict([data_dict])
    #data_df = data_df[scale]
    prediction = model.predict(data_df)

    if (prediction==1):
         prediction = "This customer is likely to be churned!!"
    else:
         prediction= "This customer is likely to continue!!" 
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    