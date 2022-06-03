from ..common import UNUSED_COLUMNS, parse_time_updated ,parse_time_publish
import  numpy as np
def preprocess(data):
    parse_time_updated(data)
    parse_time_publish(data)

def time_section(data):
    data["section"] = np.zeros(data.shape[0])
    data.section[(data['pub_hour'] >= 8) & (data['pub_hour'] <= 10)] = 1
    data.section[(data['pub_hour'] >= 12) & (data['pub_hour'] <= 14)] = 2
    data.section[(data['pub_hour'] >= 16) & (data['pub_hour'] <= 18)] = 3

    # used to seperate to all time section
    # print(data["section"].value_counts())
    return data

def convert_weekday(data):
    days = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
    for day in days:
        data.pub_day[data.pub_day == day] = days[day]
    return data


