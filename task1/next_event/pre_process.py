from task1.common import UNUSED_COLUMNS, parse_time
import numpy as np
import pandas as pd

GROUP_COL_NAME = 'test_set'

def preprocess(data):
    parse_time(data)
    data = data[data['linqmap_city'] == 'תל אביב - יפו']
    
    data = data.drop(columns=UNUSED_COLUMNS)
    data.dropna(inplace=True)
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

# def clean_data():
    


# def structure_data():
    # pass

# def add_features():
    # pass