import os
import pickle
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

#from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor


df_final = pd.read_csv("ready_to_learn_csv.csv")

y = df_final["Price"]
X = df_final.drop(["Price"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, shuffle=True) 

def preprocess():
    """
    this function will preprocess the data, it deals with nan values, non numerical values and normalize the columns
    """
    global X_train
    global X_test

    #deal wit the missings values in the coluln swimming-pool
    X_train["Swimming_pool" + "_was_missing"] = X_train["Swimming_pool"].isnull()
    X_test["Swimming_pool" + "_was_missing"] = X_test["Swimming_pool"].isnull()
    X_train['Swimming_pool'].fillna(False, inplace=True) #missing value set to False
    X_test['Swimming_pool'].fillna(False, inplace=True) #missing value set to False


    #deal with categorical variable in type of property
    #appartment and house 
    X_train = X_train.replace(
        {
            "Type_of_property": {
                "APARTMENT": 1,
                "HOUSE": 2,
            }
        }
    )
    X_test = X_test.replace(
        {
            "Type_of_property": {
                "APARTMENT": 1,
                "HOUSE": 2,
            }
        }
    )

    #swimming pool /wasmissing integers and not booleans
    X_train = X_train.replace(
        {
           "Swimming_pool": {
            True : 1,
            False : 0,
           } 
        }
    )
    X_test = X_test.replace(
        {
           "Swimming_pool": {
            True : 1,
            False : 0,
           } 
        }
    )
    X_train = X_train.replace(
        {
           "Swimming_pool_was_missing": {
            True : 1,
            False : 0,
           } 
        }
    )
    X_test = X_test.replace(
        {
           "Swimming_pool_was_missing": {
            True : 1,
            False : 0,
           } 
        }
    )


if __name__ == "__main__":
    preprocess()

    #sort is used to have a simple way to be coherent through all the files
    X_train.sort_index(axis=1, inplace=True)
    X_test.sort_index(axis=1, inplace=True)

    #model = XGBRegressor(learning_rate=0.07, max_depth=7, min_child_weight=4, n_estimators=500, subsample=0.7, colsample_bytree=0.7,)
    model = RandomForestRegressor(n_estimators=5, random_state=0)
    # training of tthe model
    model.fit(X_train, y_train) 
    #save the model
    pickle.dump(model, open('model.pkl', "wb"))

    # testing of the model
    score = model.score(X_test, y_test)
    print("efficiency of the model used for the API:", score)