from task1.common import load_data, data_split
from task1.event_dist.pre_process import preprocess, time_section
# from .utils import get_arguments
import numpy as np

def main():
    # args = get_arguments()
    data = load_data()
    train, dev, test = data_split(data)
    fit(train)
    predict(train)



def fit(data):
    df = preprocess(data)
    print(df.dtypes)
    sectioned = time_section(df)
    print(sectioned.head(200))

    #[ACCIDENT, JAM, ROAD_CLOSED, WEATHERHAZARD]
    return {}

    # model = fit(df)
    # save_model(model)

def predict(data):
    df = preprocess(data)
    df = time_section(df)
    predict_day(df)
    # model = load_model()
    # pred = predict(model, df)

    #[ACCIDENT, JAM, ROAD_CLOSED, WEATHERHAZARD]
    #[ACCIDENT, JAM, ROAD_CLOSED, WEATHERHAZARD]
    #[ACCIDENT, JAM, ROAD_CLOSED, WEATHERHAZARD]

def predict_day(data):

    arr_events = dummy_average_by_section(data)

    return arr_events


def dummy_average_by_section(data):
    arr_events = []
    for time_sec in range(1, 4):
        cur = data[data["section"] == time_sec]

        observations = cur.shape[0]
        dict_i = cur["linqmap_type"].value_counts().to_dict()
        events_in_sec = [dict_i['ACCIDENT'], dict_i['JAM'],
                         dict_i['ROAD_CLOSED'], dict_i['WEATHERHAZARD']]
        events_in_sec = np.asarray(events_in_sec)
        events_in_sec = events_in_sec / observations
        events_in_sec = events_in_sec.round(2)

        arr_events.append(events_in_sec.tolist())
    return arr_events


if __name__ == "__main__":
    main()
