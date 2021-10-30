import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

def load_and_process(file_name):
    data = pd.read_csv(file_name)
    df = data.drop(["instant"],axis=1)
    z = np.abs(stats.zscore(df["casual"]))
    df = df[(z < 1.7)]
    return df


