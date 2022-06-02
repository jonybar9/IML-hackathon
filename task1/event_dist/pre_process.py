import pandas as pd


def preprocess(data, question):
    return clean_data(data, question)


def clean_data(data, question):
    """

    Parameters
    ----------
    question: "Q1" or "Q2" question we want to clean the data for
    Returns: clean data frame
    -------

    """
    # convert date to datetime format and add time features
    data['update_date'] = pd.to_datetime(data['update_date'], unit='ms')
    data['day_of_week'] = data['update_date'].dt.day_name()
    data['hour'] = data['update_date'].dt.hour

    # clean data uniquely for Question 1
    if question == 'Q1':
        data = data[data['linqmap_city'] == 'תל אביב - יפו']

    # clean data uniuqely for Question 2
    if question == 'Q2':
        columns_to_drop_Q2 = ['linqmap_subtype', 'linqmap_magvar', 'x', 'y']
        data = data.drop(columns=columns_to_drop_Q2)

    # remove columns we don't want
    columns_to_drop = ['OBJECTID', 'pubDate', 'linqmap_reportDescription',
                          'linqmap_reportDescription', 'linqmap_street', 'linqmap_nearby',
                          'linqmap_reportMood', 'linqmap_roadType', 'linqmap_reportMood',
                          'linqmap_reportRating', 'linqmap_expectedBeginDate', 'linqmap_expectedEndDate',
                          'linqmap_reliability', 'nComments', 'update_date', 'linqmap_city']
    data = data.drop(columns=columns_to_drop)
    data.dropna(inplace=True)

    return data


def structure_data():
    pass


def add_features():
    pass
