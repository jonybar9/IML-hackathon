import pandas as pd
import numpy as np
from task1.next_event.utils import load_data, data_split
from task1.next_event.pre_process import preprocess
from sklearn.tree import DecisionTreeClassifier


def main():
    # args = get_arguments()
    data = load_data(r"..\datasets\waze_data.csv")
    data = preprocess(data)
    train_data, dev, test = data_split(data)
    type_classefier_model(train_data, dev, test)

def type_classefier_model(train: pd.DataFrame, dev: pd.DataFrame, test: pd.DataFrame):
    datasets = [train, dev, test]
    for data_set in datasets:
        data_set = extra_preprocessing(data_set)
        break
    family_samples, family_labels = split_data_for_event_classifiers(train)
    # PART ONE: Classification of Event Type: Using decision tree
    baseline_family_tree = DecisionTreeClassifier(max_depth=5)
    baseline_family_tree.fit(family_samples, family_labels.astype('string'))
    #family_prediction = baseline_family_tree.predict()
    family_prediction = family_labels
    # PART TWO: Classification of Event Sub Type: Using Mean
    # for all events from this family, return the most common subtype
    most_common_sub_types = train.groupby(['linqmap_type'])['linqmap_subtype'].agg(pd.Series.mode).to_frame()
    most_common_sub_types = most_common_sub_types.to_dict(orient='index')

    # sub_type_prediction: for each value in family_prediction match the most common val from groupby
    func = (lambda item: most_common_sub_types[item]['linqmap_subtype'])
    sub_type_prediction = np.array(list(map(func, family_prediction)))
    return family_prediction, sub_type_prediction


def extra_preprocessing(data: pd.DataFrame):
    def convert_weekday(data):
        days = {'Sunday':1, 'Monday':2, 'Tuesday':3, 'Wednesday':4, 'Thursday':5, 'Friday':6, 'Saturday':7}
        for day in days:
            data.day_of_week[data.day_of_week == day] = days[day]
        return data
    data = convert_weekday(data)
    return data

def split_data_for_event_classifiers(data: pd.DataFrame):
    """
    splits the data for the event types classifiers
    :param data: pandas.DataFrame
    :return: data_subsets: Tuple[family_samples, family_labels]
    family_samples - events without family-type and sub-type columns
    family_labels - labels of event-family
    """
    family_labels = data.linqmap_type
    family_samples = data.drop(['linqmap_type','linqmap_subtype'], axis=1)
    return family_samples, family_labels

def fit(data):
    df = preprocess(data)
    # model = fit(df)
    # save_model(model)


def predict(data):
    df = preprocess(data)
    # model = load_model()
    # pred = predict(model, df)


if __name__ == "__main__":
    np.random.seed(0)
    main()