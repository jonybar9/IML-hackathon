from task1.common import load_data
from task1.next_event.pre_process import preprocess

# from .utils import get_arguments


def main():
    # args = get_arguments()
    data = load_data()
    fit(data)


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