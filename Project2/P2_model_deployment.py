#!/usr/bin/python

import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import sys
import os


def predict_proba(year, mileage, state, make , model):

    clf = joblib.load(os.path.dirname(__file__) + '/pricemodeling_factorize.pkl') 
    
    df = {'year': [year], 'mileage': [mileage], 'state': [state], 'make': [make], 'model': [model]}
    df = pd.DataFrame(df)

    df['state'] = pd.factorize(df['state'])[0]
    df['make'] = pd.factorize(df['make'])[0]
    df['model'] = pd.factorize(df['model'])[0]

    p1 = clf.predict(df.iloc[:,])[0:1]
        
    return p1


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add an URL')
        
    else:

        year =      sys.argv[1]
        mileage =   sys.argv[2]
        state =   sys.argv[3]
        make =   sys.argv[4]
        model =   sys.argv[5]
        
        
        p1 = predict_proba(year, mileage, state, make , model)
        
        print(year, mileage)
        print('Probability of Phishing: ', p1)