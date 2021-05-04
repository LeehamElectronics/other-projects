import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def last_ten(file, number_of_lines):
    f = open(file, "r")
    lines = []
    num_lines = sum(1 for line in open('log.txt'))
    for position, line in enumerate(f):
        for i in range(num_lines-number_of_lines, num_lines):
            if position == i:
                print(line, end='')
                lines.append(line)
    return lines

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event.event_type, event.src_path)

    def on_created(self, event):
        print("on_created", event.src_path)

    def on_deleted(self, event):
        print("on_deleted", event.src_path)

    def on_modified(self, event):
        print("on_modified", event.src_path)
        if event.src_path == "./log.txt":
            last_ten('log.txt', 10)
    def on_moved(self, event):
        print("on_moved", event.src_path)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='./', recursive=False)
observer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()