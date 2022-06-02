import pandas as pd

def parse_time(data):
    # convert date to datetime format and add time features
    data['update_date'] = pd.to_datetime(data['update_date'], unit='ms')
    data['day_of_week'] = data['update_date'].dt.day_name()
    data['hour'] = data['update_date'].dt.hour


UNUSED_COLUMNS = ['OBJECTID', 'pubDate', 'linqmap_reportDescription',
                          'linqmap_reportDescription', 'linqmap_street', 'linqmap_nearby',
                          'linqmap_reportMood', 'linqmap_roadType', 'linqmap_reportMood',
                          'linqmap_reportRating', 'linqmap_expectedBeginDate', 'linqmap_expectedEndDate',
                          'linqmap_reliability', 'nComments', 'update_date', 'linqmap_city']


def load_data():
    return pd.read_csv("../datasets/waze_data.csv")
