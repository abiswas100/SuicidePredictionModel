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

def find_indivitual_probability(train):
    print(train)
    a,b,c,d,e = 0,0,0,0,0
    for i, j in train.iterrows(): 
        if   j[1] ==  0: a = a + j[0]
        elif j[1] ==  1: b = b + j[0]
        elif j[1] ==  2: c = c + j[0]
        elif j[1] ==  3: d = d + j[0]
        elif j[1] ==  4: e = e + j[0]

    total = a+b+c+d+e
    # print(total)   
    prob_a = a/total
    prob_b = b/total
    prob_c = c/total
    prob_d = d/total
    prob_e = e/total
    
    # print(prob_a,prob_b,prob_c,prob_d,prob_e)

    return prob_a,prob_b,prob_e,prob_d,prob_e    
    
def main():
    df = pd.read_csv("Social.csv")
          
    Social_train = df.loc[(df['Year'] >= 2001) & (df['Year'] <= 2010)]
    Social_test = df.loc[(df['Year'] >= 2011) & (df['Year'] <= 2012)]
    
    '''
    Adding Encoding to Education and Gender 
    '''
    for ind,row in Social_train.iterrows():
        Social_train.loc[ind,"Cataegory"] = encoding(Social_train.loc[ind,"Type"])
    Social_train = Social_train.astype({"Cataegory": int})
    print(Social_train)
    Social_train = Social_train.drop(['State','Year','Type','Type_code','Gender','Age_group'],axis='columns')
    
    # Getting the Averages for each social types            
    prob_a,prob_b,prob_c,prob_d,prob_e =  find_indivitual_probability(Social_train)
    total_per_cataegory = []
    total_per_cataegory.append(prob_a)
    total_per_cataegory.append(prob_b)
    total_per_cataegory.append(prob_c)
    total_per_cataegory.append(prob_d)
    total_per_cataegory.append(prob_e)
        
if __name__ == "__main__":
    main()




    
