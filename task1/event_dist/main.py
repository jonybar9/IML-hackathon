from task1.common import load_data
# from .utils import get_arguments


def main():
    # args = get_arguments()
    data = load_data()


def fit(data):
    df = preprocess(data)
    model = fit(df)
    save_model(model)

def predict(data):
    df = preprocess(data)
    model = load_model()
    pred = predict(model, df)



if __name__ == "__main__":
    main()