from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def last_ten(file, number_of_lines):
    h = open("log10.txt", "w")
    h.write("")
    f = open(file, "r")
    lines = []
    num_lines = sum(1 for line in open('log.txt'))
    for position, line in enumerate(f):
        for i in range(num_lines - number_of_lines, num_lines):
            if position == i:
                print(line, end='')
                g = open("log10.txt", "a")  # write file where the lines are sent to
                g.write(line)
                lines.append(line)
    return lines


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "./log.txt":
            last_ten('log.txt', 10)  # file and amount of lines to read


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='./', recursive=False)
observer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
