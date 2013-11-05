import requests
import time

class Timer(object):

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


def test_block():
    for i in xrange(10000):
        requests.get("http://127.0.0.1:8080")


if __name__ == "__main__":
    with Timer() as t:
        test_block()
    print t.interval
