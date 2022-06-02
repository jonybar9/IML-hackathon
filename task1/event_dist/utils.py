import numpy as np
import pandas as pd

TRAIN_SIZE = 0.7
TEST_SIZE = 0.2

def data_split(data: pd.DataFrame):
    """
    splits the preprocessed data to train, dev, test datasets
    Parameters
    ----------
    filename: str
        data - DataFrame of all the training data

    Returns
    -------
        train, dev, test - DataFrame, DataFrame, DataFrame
    """
    np.random.seed(0)
    test = data.sample(frac=TEST_SIZE)
    train_dev = data.drop(index=test.index)
    train = train_dev.sample(frac=TRAIN_SIZE)
    dev = train_dev.drop(index=train.index)
    return train, dev, test

