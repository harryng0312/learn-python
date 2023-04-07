from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future, wait
# from collections.abc import Mapping
import datetime
import time
import os
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../', '../')))
from module.util.logger_conf import logger

TOTAL: int = 0


def thread_function(param: list[str]) -> None:
    logger.info(f"into thread function{param} at {datetime.datetime.now()}")
    time.sleep(2.0)
    logger.info(f"out to thread function{param} at {datetime.datetime.now()}")
    pass


def thread_function_2(param1: int, param2: int) -> None:
    global TOTAL
    TOTAL += param1 * param2
    time.sleep(0.5)
    pass


def single_thread() -> None:
    x: Thread = Thread(target=thread_function, args=(["test 1", "test 2"],))
    logger.info(f"Start:\t\t{datetime.datetime.now()}")
    x.start()
    logger.info(f"Finish:\t{datetime.datetime.now()}")
    x.join()
    pass


def multi_thread() -> None:
    count: int = 3
    threads: list[Thread] = []
    global TOTAL
    with ThreadPoolExecutor(max_workers=4) as pool:
        # with ProcessPoolExecutor(max_workers=3) as pool:
        for _ in pool.map(thread_function_2, (1, 1, 1, 1), (1, 1, 1, 1), timeout=0.6): pass
        pass
    logger.info(f"resource:{TOTAL}")
    pass


if __name__ == "__main__":
    nowStr: str = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    # single_thread()
    multi_thread()
    pass

# print(f"__name__:{__name__}")
