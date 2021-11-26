import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

def load_and_process_simplify(file_name):
    data = pd.read_csv(file_name)
    z = np.abs(stats.zscore(data["casual"]))
    data = data.drop(["instant","weathersit","temp","atemp","hum","windspeed"],axis=1)[(z < 1.7)]
    data["season"] = data["season"].replace( {1:"springer", 2:"summer", 3:"fall", 4:"winter"})
    data["weekday"] = data["weekday"].replace( {0:"sunday", 1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday"})
    return data
    


def load_and_process(file_name):
    data = pd.read_csv(file_name)
    df = data.drop(["instant"],axis=1)
    z = np.abs(stats.zscore(df["casual"]))
    df = df[(z < 1.7)]
    return df