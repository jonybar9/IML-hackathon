from ..common import UNUSED_COLUMNS, parse_time
import  numpy as np

def preprocess(data):
    parse_time(data)

    columns_to_drop_Q2 = ['linqmap_subtype', 'linqmap_magvar', 'x', 'y']
    data = data.drop(columns=columns_to_drop_Q2)
    data = data.drop(columns=UNUSED_COLUMNS)
    data.dropna(inplace=True)
    return data


def time_section(data):
    data["section"] = np.zeros(data.shape[0])
    data.section[(data['hour'] >= 8) & (data['hour'] <= 10)] = 1
    data.section[(data['hour'] >= 12) & (data['hour'] <= 14)] = 2
    data.section[(data['hour'] >= 16) & (data['hour'] <= 18)] = 3

    # used to seperate to all time section
    # print(data["section"].value_counts())
    return data

# def clean_data(data):
#     """

#     Parameters
#     ----------
#     Returns: clean data frame
#     -------

#     """
    # parse_time(data)


    # remove columns we don't want

    # return data

# def structure_data():
#     pass

# def add_features():
#     pass

