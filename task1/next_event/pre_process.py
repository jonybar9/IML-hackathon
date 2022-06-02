from ..common import UNUSED_COLUMNS, parse_time
import pandas as pd

def preprocess(data):
    parse_time(data)
    data = data[data['linqmap_city'] == 'תל אביב - יפו']
    
    data = data.drop(columns=UNUSED_COLUMNS)
    data.dropna(inplace=True)

    data = pd.concat([data, pd.get_dummies(data['linqmap_type'], drop_first=True)], axis=1)
    data = pd.concat([data, pd.get_dummies(data['hour'], drop_first=True)], axis=1)
    data = data.drop(columns=["linqmap_type", "linqmap_subtype", "day_of_week", 'hour'])

    return data

# def group_by_time(data):


# def clean_data():
    


# def structure_data():
    # pass

# def add_features():
    # pass