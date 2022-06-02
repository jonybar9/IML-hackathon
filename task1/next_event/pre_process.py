from ..common import UNUSED_COLUMNS, parse_time
import pandas as pd
import numpy as np


def preprocess(data):
    parse_time(data)
    data = data[data['linqmap_city'] == 'תל אביב - יפו']

    data = data.drop(columns=UNUSED_COLUMNS)
    data.dropna(inplace=True)

    data = pd.concat([data, pd.get_dummies(data['linqmap_type'], drop_first=True)], axis=1)
    data = pd.concat([data, pd.get_dummies(data['hour'], drop_first=True)], axis=1)
    data = data.drop(columns=["linqmap_type", "linqmap_subtype", "day_of_week", 'hour'])

    return data


def split_data_to_X_and_y(lst):
    """
    lst: list of dataframes with five rows
    returns: X: numpy matrix where each row is four samples flattened
             y: pandas DataFrame where each row is the labels we need to predict of corresponding row in X
    """
    X = np.array([df[:4].to_numpy().flatten() for df in lst])
    y = [df[4:] for df in lst]
    y = pd.concat(y)
    y = y[['linqmap_type', 'linqmap_subtype', 'x', 'y']]  # keep only labels we need to predict
    return X, y




# def group_by_time(data):


# def clean_data():


# def structure_data():
# pass

# def add_features():
# pass
