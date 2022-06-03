import pandas as pd
import numpy as np
from task1.next_event.utils import load_data, data_split
from task1.next_event.pre_process import preprocess, bulk_bootsraping, \
    group_by_bulk, split_train_data_to_X_and_y, merge_test_data
#from task1.next_event.pre_process import preprocess
from .pre_process import preprocess
from .pre_process import bulk_bootsraping, group_by_bulk, split_train_data_to_X_and_y, merge_test_data
from catboost import CatBoostClassifier, CatBoostRegressor, Pool
from catboost import CatBoostClassifier, CatBoostRegressor


def main1(train_path="waze_data.csv", test_path="waze_take_features.csv"):
    # args = get_arguments()
    data = load_data(train_path)
    data = preprocess(data)
    train_data, dev, test = data_split(data)
    real_test = load_data(test_path)
    real_test = preprocess(real_test)

    #X_test = merge_test_data(bulk_bootsraping(real_test))

    train_with_groups = bulk_bootsraping(train_data)
    grouped_train = group_by_bulk(train_with_groups)
    X_train, y_train, categorial_indices = split_train_data_to_X_and_y(grouped_train)

    dev_with_groups = bulk_bootsraping(dev)
    grouped_dev = group_by_bulk(dev_with_groups)
    X_dev, y_dev, categorial_indices  = split_train_data_to_X_and_y(grouped_dev)

    categorial_indices = ['day_of_week_0', 'day_of_week_1', 'day_of_week_2', 'day_of_week_3',
                          'linqmap_type_0', 'linqmap_type_1', 'linqmap_type_2', 'linqmap_type_3',
                          'linqmap_subtype_0', 'linqmap_subtype_1', 'linqmap_subtype_2', 'linqmap_subtype_3',
                          ]

    types_pred, subtypes_pred = type_classefier_model(train_data, X_dev,y_dev, X_train, y_train, categorial_indices)
    #types_pred, subtypes_pred = type_classefier_model(train_data, X_test,y_dev, X_train, y_train, categorial_indices)

    #predictions = regressor_x_y(X_train, y_train, X_dev, y_dev, categorial_indices)
    result = np.concatenate((types_pred, subtypes_pred),axis=1)
    result = pd.DataFrame(result)
    result['x'] = train_data.x.mean()
    result['y'] = train_data.y.mean()
    result.to_csv('predictions.csv', header=False, index=False)

def regressor_x_y(X_train, y_train, X_dev, y_dev, cat_indices):
    model_x = CatBoostRegressor(iterations=100)
    model_y = CatBoostRegressor(iterations=100)
    #cat_indices = pd.DataFrame(X_train).select_dtypes("O").columns
    model_x.fit(pd.DataFrame(X_train), y_train[2], cat_features=cat_indices)
    model_y.fit(pd.DataFrame(X_train), y_train[3], cat_features=cat_indices)

    return model_x.predict(pd.DataFrame(X_dev)), model_y.predict(pd.DataFrame(X_dev))


def type_classefier_model(train: pd.DataFrame, flatten_dev: pd.DataFrame,
                          fifth_dev: pd.DataFrame, flatten: pd.DataFrame, fifth: pd.DataFrame, cat_indices: list):
    """
    This function fits over flattened groups data to predict the event family and sub-type of the fifth event
    :param train: training data - preprocessed but not flattened/aggregated by group
    :param flatten_dev: dev data preprocessed and flattened by group
    :param fifth_dev: dev labels preprocessed and by group
    :param flatten: training data preprocessed and flattened by group
    :param fifth: training labels preprocessed and by group
    :return: Tuple[event family prediction, event subtype prediction]
    """
    train_labels = fifth.linqmap_type
    def catboost_classifier():
        baseline_family_tree = CatBoostClassifier(iterations=100)
        baseline_family_tree.fit(flatten, train_labels, cat_features=cat_indices)
        family_prediction = baseline_family_tree.predict(flatten_dev)
        return family_prediction

    def match_common_subtype(pred):
        subtypes = pred.copy()
        most_common_sub_types = train.groupby(['linqmap_type'])['linqmap_subtype'].agg(pd.Series.mode).to_dict()
        most_common_sub_types['ACCIDENT'] = 'ACCIDENT_MAJOR'
        for family in np.unique(train_labels):
            subtypes = np.where(subtypes == family,most_common_sub_types[family] ,subtypes)
        return subtypes

    def subtype_classifiers(predicted_types):
        # fit:
        families = {}
        for family in np.unique(train_labels):
            family_data = train[train.linqmap_type == family]
            family_labels = family_data.drop('linqmap_subtype')
            model = CatBoostClassifier(iterations=100)
            model.fit(flatten, train_labels, cat_features=['linqmap_type', 'day_of_week'])
            families[family] = model

        # prediction - this will not work
        func = (lambda item: families[item].predict(dev))
        sub_type_prediction = np.array(list(map(func, predicted_types)))

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

main1()