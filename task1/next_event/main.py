import pandas as pd
import numpy as np
from task1.next_event.utils import load_data, data_split
from task1.next_event.pre_process import preprocess
from catboost import CatBoostClassifier


def main():
    # args = get_arguments()
    data = load_data(r"..\datasets\waze_data.csv")
    data = preprocess(data)
    train_data, dev, test = data_split(data)
    type_classefier_model(train_data, test, train_data, train_data)

def type_classefier_model(train: pd.DataFrame, dev: pd.DataFrame, flatten: pd.DataFrame, fifth: pd.DataFrame):
    train_labels = fifth.linqmap_type

    def catboost_classifier():
        baseline_family_tree = CatBoostClassifier(iterations=100)
        baseline_family_tree.fit(flatten, train_labels, cat_features=['linqmap_type','linqmap_subtype','day_of_week'])
        family_prediction = baseline_family_tree.predict(dev)
        return family_prediction

    def match_common_subtype(prediction):
        most_common_sub_types = train.groupby(['linqmap_type'])['linqmap_subtype'].agg(pd.Series.mode).to_frame()
        most_common_sub_types = most_common_sub_types.to_dict(orient='index')
        func = (lambda item: most_common_sub_types[item]['linqmap_subtype'])
        sub_type_prediction = np.array(list(map(func, prediction)))
        return sub_type_prediction

    prediction = catboost_classifier()
    return prediction , match_common_subtype(prediction)


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