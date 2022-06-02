from ..common import UNUSED_COLUMNS, parse_time

def preprocess(data):
    parse_time(data)
    data = data[data['linqmap_city'] == 'תל אביב - יפו']
    
    data = data.drop(columns=UNUSED_COLUMNS)
    data.dropna(inplace=True)
    return data

# def group_by_time(data):


# def clean_data():
    


# def structure_data():
    # pass

# def add_features():
    # pass