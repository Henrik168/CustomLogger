import CustomLogger
from time import sleep

log = CustomLogger.getLogger(name="TestLogger")


def main():
    for i in range(10):
        log.info(f"Test {i}")
        sleep(1)


if __name__ == "__main__":
    main()
