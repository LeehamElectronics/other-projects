from time import sleep, perf_counter


def task():
    print('Starting a task...')
    sleep(1)
    print('done')


start_time = perf_counter()  # get the value of the performance counter by calling the perf_counter() function:

task()  # call the task() function twice
task()

end_time = perf_counter()  # get the value of the performance counter calling the perf_counter() function

print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')  # output the time that takes to complete
# running the task() function twice:

# First, the task() function executed and slept for one second. Then it executed a second time and also slept for
# another second. Finally, the program completes. When the task() function called the sleep() function,
# the CPU didn’t do anything. This is not efficient. This program has one process with a single thread,
# which is called the main thread. Because the program has only one thread, it’s called the single-threaded program.
