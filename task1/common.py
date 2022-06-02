import pandas as pd

def parse_time(data):
    # convert date to datetime format and add time features
    data['pubDate'] = pd.to_datetime(data['pubDate'])
    # create dummy variables for day of week
    data['day_of_week'] = data['pubDate'].dt.day_name()
    data = pd.concat([data, pd.get_dummies(data['day_of_week'], drop_first=True)], axis=1)
    data.drop(columns=['day_of_week'], inplace=True)

    data['hour'] = data['pubDate'].dt.hour


UNUSED_COLUMNS = ['OBJECTID', 'pubDate', 'linqmap_reportDescription',
                          'linqmap_reportDescription', 'linqmap_street', 'linqmap_nearby',
                          'linqmap_reportMood', 'linqmap_roadType', 'linqmap_reportMood',
                          'linqmap_reportRating', 'linqmap_expectedBeginDate', 'linqmap_expectedEndDate',
                          'linqmap_reliability', 'nComments', 'update_date', 'linqmap_city']


def load_data():
    return pd.read_csv("../datasets/waze_data.csv")
