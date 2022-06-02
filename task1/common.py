import pandas as pd
import pickle

def parse_time(data):
    # convert date to datetime format and add time features
    data['pubDate'] = pd.to_datetime(data['pubDate'])
    # create dummy variables for day of week
    data['day_of_week'] = data['pubDate'].dt.day_name()
    data['hour'] = data['pubDate'].dt.hour

# duplicated code because of different column names and the hour being too late.
def parse_time_publish(data):
    # convert date to datetime format and add time features
    data['pubDate'] = pd.to_datetime(data['pubDate'])
    data['pub_day'] = data['pubDate'].dt.day_name()
    data['pub_hour'] = data['pubDate'].dt.hour


def parse_time_updated(data):
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

def save_model(filename, model):
    pickle.dump(model, open(filename, 'wb'))

def load_model(filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model