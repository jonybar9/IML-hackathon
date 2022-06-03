import sys
from task1.next_event.main import predict as predict_next
from task1.event_dist.main import predict as dist_predict

def main():
    args = sys.argv
    test_path = args[1]
    task1_test_path = args[2]
    task2_dates_path = args[3]
    task2_dates = get_dates(task2_dates_path)

    dist_predict(test_path)



def get_dates(task2_dates_path):
    return task2_dates_path


if __name__ == "__main__":
    main()