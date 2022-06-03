import sys
import numpy as np
from task1.next_event.task_1 import predict as predict_next
from task1.event_dist.task_2 import predict as dist_predict
from task1.next_event import task_1
from task1.event_dist import task_2

def main():
    args = sys.argv
    train_path = args[1]
    test_path = args[2]
    task2_dates_path = args[3]
    #dist_predict(test_path)
    try:
        task_1.main1(train_path, test_path)
    except Exception:
        pass

    try:
        task_2.main2(task2_dates_path)
    except Exception:
        pass

if __name__ == "__main__":
    np.random.seed(0)
    main()