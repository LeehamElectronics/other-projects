# Import Module
from tkinter import *
import time
from threading import *
from time import sleep, perf_counter
import itertools

# Create Object
root = Tk()

# Set geometry
root.geometry("200x100")

def to_infinity():
    index=0
    while 1:
        yield index
        index += 1
    print(i)


def read():
    f = open("log10.txt", "r")  # opens log10.txt in read mode
    print(f.read())  # sets log_list to the contents of log10.txt
    sleep(1)

start_time = perf_counter()

threads = []

for n in range(1, 2):
    t = Thread(target=read)
    threads.append(t)
    t.start()

for i in to_infinity():
    t.join()

# for i in itertools.count():
#     t.join()
#     t.join()
#     t.join()
#     t.join()
#     t.join()


end_time = perf_counter()
print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')


# Create Button


# Execute Tkinter
root.mainloop()