import os
import sys
from datetime import datetime

args = sys.argv

dirs = []
file_name = None

if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args and args.index("-f") > d_index:
        f_index = args.index("-f")
        dirs = args[d_index + 1:f_index]
    else:
        dirs = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

path = ""
if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

if file_name:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    file_path = os.path.join(path, file_name)

    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for number, line in enumerate(lines, 1):
            file.write(f"{number} {line}\n")
