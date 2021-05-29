from threading import *
from time import sleep, perf_counter


threads = []

x = 0


def test1():
    v = 1
    a = 0
    while v <= 10:
        sleep(0.08)
        print("loop a", a)
        a = a + 1


def test2():
    v = 1
    a = 0
    while v <= 10:
        sleep(0.08)
        print("loop b", a)
        a = a + 1


def thread():
    t1 = Thread(target=test1)
    t2 = Thread(target=test2)
    t1.start()
    sleep(0.004)
    t2.start()


thread()

