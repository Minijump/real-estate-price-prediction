import pickle
import pandas as pd
#import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor


def predict(data: dict) -> float:
    """ 
    this function will use tha data given by the user and the train model to return a prediction of price
    """
    #create and load the model  
    random_forest_model = pickle.load(open('model.pkl', "rb"))

    #create a dataframe from the dictionnary given in argument
    df = pd.DataFrame.from_dict(data, orient='index').T
    df.sort_index(axis=1, inplace=True)

    #predict the price----------------------probleme ici-------------------
    price = float(random_forest_model.predict(df)[0])

    return price