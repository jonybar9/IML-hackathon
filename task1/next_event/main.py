import pandas as pd
from .utils import load_data
from sklearn.tree import DecisionTreeClassifier


def main():
    # args = get_arguments()
    data = load_data() 
    train_data, dev, test = split_data(data)
    test = load_data('waze_take_features.csv')
    # add preprocessing

    event_family, event_subtype = split_data(train_data)

    # PART ONE: Classification of Event Type: Using decision tree
    baseline_family_tree = DecisionTreeClassifier(max_depth=5)
    baseline_family_tree.fit(event_family[0], event_family[1])
    family_prediction = baseline_family_tree.predict(test)

    # PART TWO: Classification of Event Sub Type: Using Mean
    # for all events from this family, return the most common subtype
    most_common_sub_types = train_data.groupby(['linqmap_type'])['linqmap_subtype'].agg(pd.Series.mode).to_frame()
    #sub_type_prediction: for each value in family_prediction match the most common val from groupby


def split_data(data: pd.Dataframe):
    """
    splits the data for the event types classifiers
    :param data: pandas.DataFrame
    :return: data_subsets:
    Tuple of 2 Tuples: first for event family and second for event sub-type
    each inner Tuple contains X_train and y_train
    """
    raise NotImplementedError


def fit(data):
    df = preprocess(data)
    print(df.head(100))
    # model = fit(df)
    # save_model(model)


def predict(data):
    df = preprocess(data)
    # model = load_model()
    # pred = predict(model, df)


if __name__ == "__main__":
    main()