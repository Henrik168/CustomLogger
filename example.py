import CustomLogger
import example_module
from time import sleep

log = CustomLogger.getLogger(level=10)


def next_rollover():
    import datetime
    last_rollover = datetime.datetime.now()
    next_day = last_rollover + datetime.timedelta(days=1)
    return datetime.datetime(next_day.year, next_day.month, next_day.day)


def main():
    print(next_rollover())
    example_module.test()
    for i in range(10):
        log.info(f"Test {i}")
        sleep(1)


if __name__ == "__main__":
    main()
