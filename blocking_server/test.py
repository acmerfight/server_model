import requests
import time

def test_block():
    for i in xrange(5):
        requests.get("http://127.0.0.1:9000")


if __name__ == "__main__":
    time_start = time.time()
    test_block()
    time_end = time.time()
    print time_end - time_start
