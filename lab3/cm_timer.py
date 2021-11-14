import datetime
import time


class cm_timer:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def __enter__(self):
        self.start_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type, exc_val, exc_tb)
        else:
            print('time: {}'.format((datetime.datetime.now() - self.start_time).seconds))


def main():
    with cm_timer():
        time.sleep(7)


if __name__ == "__main__":
    main()
