from task1.common import load_data
from task1.event_dist.utils import data_split
from task1.event_dist.pre_process import preprocess, time_section, convert_weekday
# from .utils import get_arguments
import numpy as np
from collections import defaultdict
import os as os


#dates = ["05.06.2022", "07.06.2022", "09.06.2022"]
dates = ["2022/06/05", "2022/06/07", "2022/06/09"]



def date_cannonical(dateslist):
    import copy
    reformated = []
    #YYYY/MM/DD to dd.mm.yyyy
    new_dateslist = copy.deepcopy(dateslist)
    for item in new_dateslist:
        reformated.append(item[8:] + "." + item[5:7] + "." + item[0:4])

    return reformated

def main():
    # args = get_arguments()
    data = load_data()
    n_rows = data.shape[0]
    train, dev, test = data_split(data)
    events_by_day, sections_scalars = fit(train, n_rows)

    # change dates to dd.mm.yyyy format
    cannonical_dates = date_cannonical(dates)
    predict(dates, events_by_day, sections_scalars)

def fit(data , nrows):
    df = preprocess(data)
    print(data)
    sectioned = time_section(df)

    sectioned = convert_weekday(sectioned)
    print(sectioned["section"].value_counts().sort_index())
    percents_sections = sectioned["section"].value_counts().sort_index()/sectioned.shape[0]
    sections_scalars = (percents_sections * nrows)/5
    # get the average table
    events_by_day = fit_the_day(sectioned)

    return events_by_day , sections_scalars

def predict(dates, events_by_day, sections_scalars):
    import pandas as pd
    dates_lst = pd.to_datetime(dates, dayfirst=True)
    weekday = dates_lst.day_of_week

    list_days = weekday.values.tolist()

    dates_for = pd.to_datetime(dates)
    list_days = (dates_lst.dayofweek + 1) % 7
    sections_scalars = sections_scalars.astype(int)

    print(sections_scalars.dtype)
    print(sections_scalars[1].dtype)
    for day in range(len(list_days)):
        idx = list_days[day]
        prediction = events_by_day[idx]
        print(np.round(prediction[0],2) * sections_scalars[1])
        prediction = [np.round(prediction[0],2) * sections_scalars[1],
                      np.round(prediction[1],2) * sections_scalars[2],
                      np.round(prediction[2],2)* sections_scalars[3]]
        #print(prediction)
        prediction = pd.DataFrame(prediction)


        prediction.to_csv(str(dates_for[day])[0:10] +'.csv')
    # model = load_model()
    # pred = predict(model, df)



def fit_the_day(data):
    data = convert_weekday(data)
    day_data_dist = []

    for day in range(1,8):
        new_data = data[data["pub_day"] == day]
        arr_events = dummy_average_by_section(new_data)
        day_data_dist.append(arr_events)
        print(arr_events)
    return day_data_dist

def dummy_average_by_section(data):
    arr_events = []
    for time_sec in range(1, 4):

        cur = data[data["section"] == time_sec]
        observations = cur.shape[0]

        dict_i = cur["linqmap_type"].value_counts().to_dict()

        accident = dict_i.get('ACCIDENT', 0)
        jam =  dict_i.get('JAM', 0)
        road_cloased = dict_i.get('ROAD_CLOSED', 0)
        weather = dict_i.get('WEATHERHAZARD', 0)

        events_in_sec = [accident, jam, road_cloased, weather]
        events_in_sec = np.asarray(events_in_sec)

        events_in_sec = events_in_sec / observations
        events_in_sec = np.nan_to_num(events_in_sec, nan=0.000)
        arr_events.append(events_in_sec.tolist())
    return arr_events





if __name__ == "__main__":
    main()
