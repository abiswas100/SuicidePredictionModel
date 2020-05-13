import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def encoding(x):
    if (x == 'Never Married'):
        return 0
    elif(x == 'Married'):
        return 1
    elif(x == 'Seperated'):
        return 2
    elif(x == 'Divorcee'):
        return 3
    elif (x == 'Widowed/Widower'):
        return 4


df = pd.read_csv("Social_Status.csv")


df = df.drop(['State','Year','Type_code','Age_group'],axis='columns')


social_types = df['Type'].unique()

# print(type(social_types[0]))

'''
Adding Encoding to Education and Gender 
'''
for ind,row in df.iterrows():
    df.loc[ind,"Cataegory"] = encoding(df.loc[ind,"Type"])
df = df.astype({"Cataegory": int})

# Getting the Averages for each social types
social_total = []
social_types = []
print(df)