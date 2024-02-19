import pandas as pd
import numpy as np


def read_data(file_path):
    df = pd.read_csv(file_path)
    return df


def preprocess_data(df, threshold_min=-1, threshold_max=1):
    df[(df < threshold_min) | (df > threshold_max)] = np.nan
    return df
