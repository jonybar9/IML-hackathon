import sys
from task1.next_event.main import predict as predict_next
from task1.event_dist.main import predict as dist_predict
from task1.next_event import task_1, task_2

def main():
    args = sys.argv
    train_path = args[1]
    test_path = args[2]
    task2_dates_path = args[3]
    dist_predict(test_path)
    try:
        task_1.main(train_path, test_path)
    except:
        pass

    try:
        task_2.main(task2_dates_path)
    except:
        pass

if __name__ == "__main__":
    np.random.seed(0)
    main()