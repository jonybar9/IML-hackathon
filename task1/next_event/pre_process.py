from task1.common import UNUSED_COLUMNS, parse_time
import numpy as np
import pandas as pd

GROUP_COL_NAME = 'test_set'
BULK_SIZE = 4


def preprocess(data):
    parse_time(data)
    data = data[data['linqmap_city'] == 'תל אביב - יפו']
    data = data.drop(columns=UNUSED_COLUMNS) # THIS NEEDS TO CHANGE
    # data.dropna(inplace=True)


    return data


def group_by_bulk(data_with_groups):
    bulks_list = [x for _, x in data_with_groups.groupby(data_with_groups[GROUP_COL_NAME])]
    bulks = np.array(bulks_list).shape
    return bulks


def bulk_bootsraping(data):
    col_names = list(data.columns)
    col_names.append(GROUP_COL_NAME)
    bulks_list = [data.iloc[i:i + BULK_SIZE + 1, ].copy() for i in
                  range(data.shape[0] - (BULK_SIZE + 1))]
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

# def add_dummies(df):
#
#     df = pd.concat([df, pd.get_dummies()])

def split_train_data_to_X_and_y(lst):
    """
    lst: list of dataframes with five rows
    returns: X: numpy matrix where each row is four samples flattened
             y: pandas DataFrame where each row is the labels we need to predict of corresponding row in X
    """
    y = [df[4:] for df in lst]
    y = pd.concat(y)
    d = y.shape[1]
    categorial_indices = []
    for label in ['linqmap_type','linqmap_subtype','day_of_week']:
        categorial_indices.append(list(y.columns).index(label))
        categorial_indices.append(categorial_indices[-1]+d)
        categorial_indices.append(categorial_indices[-1]+d)
        categorial_indices.append(categorial_indices[-1]+d)

    y = y[['linqmap_type', 'linqmap_subtype', 'x', 'y']]  # keep only labels we need to predict
    col_names_base = list(lst[0].columns)
    col_names = [f"{name}_{i}" for i in range(4) for name in col_names_base]

    X = np.array([df[:4].to_numpy().flatten() for df in lst])
    X = pd.DataFrame(X)
    X.columns = col_names
    a=3





    return X, y, sorted(categorial_indices)


def merge_test_data(lst):
    """
    lst: list of dataframes with five rows
    returns: X: numpy matrix where each row is four samples flattened
             y: pandas DataFrame where each row is the labels we need to predict of corresponding row in X
    """
    X = np.array([df[:4].to_numpy().flatten() for df in lst])
    return X