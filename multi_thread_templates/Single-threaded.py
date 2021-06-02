from time import sleep, perf_counter


def task():
    a = 0
    v = 0
    while v == 0:
        start_time = perf_counter()  # get the value of the performance counter by calling the perf_counter() function:
        log = "loop a" + " " + str(a)
        print(log)
        a = a + 1
        sleep(1)
        end_time = perf_counter()  # get the value of the performance counter calling the perf_counter() function
        print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')  # output the time that takes to complete

task()  # call the task()