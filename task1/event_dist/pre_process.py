from ..common import UNUSED_COLUMNS, parse_time
def preprocess(data):
    parse_time(data)

    columns_to_drop_Q2 = ['linqmap_subtype', 'linqmap_magvar', 'x', 'y']
    data = data.drop(columns=columns_to_drop_Q2)
    data = data.drop(columns=UNUSED_COLUMNS)
    data.dropna(inplace=True)
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

