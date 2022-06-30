import CustomLogger
import example_module
from time import sleep

log = CustomLogger.getLogger()


def main():
    example_module.test()
    for i in range(3):
        log.info(f"Test {i}")
        sleep(1)


if __name__ == "__main__":
    main()
