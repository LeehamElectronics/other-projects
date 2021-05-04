import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def get_last_n_lines(file_name, N):
    list_of_lines = []
    with open(file_name, 'rb') as read_obj:
        read_obj.seek(0, os.SEEK_END)
        buffer = bytearray()
        pointer_location = read_obj.tell()
        while pointer_location >= 0:
            read_obj.seek(pointer_location)
            pointer_location = pointer_location -1
            new_byte = read_obj.read(1)
            if new_byte == b'\n':
                list_of_lines.append(buffer.decode()[::-1])
                if len(list_of_lines) == N:
                    return list(reversed(list_of_lines))
                buffer = bytearray()
            else:
                buffer.extend(new_byte)
        if len(buffer) > 0:
            list_of_lines.append(buffer.decode()[::-1])
    return list(reversed(list_of_lines))

def main():
    print('** Get last 5 lines of text file or csv file **')
    last_lines = get_last_n_lines("log.txt", 5)
    print('Last 5 lines of File:')
    for line in last_lines:
        print(line)
if __name__ == '__main__':
   main()