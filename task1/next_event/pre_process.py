from task1.common import UNUSED_COLUMNS, parse_time
import numpy as np
import pandas as pd

GROUP_COL_NAME = 'test_set'

def preprocess(data):
    parse_time(data)
    data = data[data['linqmap_city'] == 'תל אביב - יפו']

    data = data.drop(columns=UNUSED_COLUMNS)
    data.dropna(inplace=True)

    data = pd.concat([data, pd.get_dummies(data['linqmap_type'], drop_first=True)], axis=1)
    data = pd.concat([data, pd.get_dummies(data['linqmap_subtype'], drop_first=True)], axis=1)
    data = pd.concat([data, pd.get_dummies(data['hour'], drop_first=True)], axis=1)
    data = data.drop(columns=["linqmap_type", "linqmap_subtype", "day_of_week", 'hour'])

    return data

def group_by_bulk():
    pass

def bulk_bootsraping(data):
    col_names = list(data.columns)
    col_names.append(GROUP_COL_NAME)
    bulks_list = [data.iloc[i:i + 5, ].copy() for i in
                  range(data.shape[0] - 5)]
    numbered_bulks = map(lambda item: _add_bulk_number(item[1], item[0]),
                         enumerate(bulks_list))
    bulks = np.array(list(numbered_bulks))
    flattened = bulks.reshape(
        (bulks.shape[0] * bulks.shape[1], bulks.shape[2]))
    bootstraped = pd.DataFrame(flattened)
    bootstraped.columns = col_names
    return bootstraped


def _add_bulk_number(df, i):
    number_col = [i for j in range(df.shape[0])]
    df.loc[:, GROUP_COL_NAME] = number_col

    return df

def split_train_data_to_X_and_y(lst):
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

def merge_test_data(lst):
    """
    lst: list of dataframes with five rows
    returns: X: numpy matrix where each row is four samples flattened
             y: pandas DataFrame where each row is the labels we need to predict of corresponding row in X
    """
    X = np.array([df[:4].to_numpy().flatten() for df in lst])
    return X


# def group_by_time(data):


# def clean_data():


# def structure_data():
# pass

# def add_features():
# pass
