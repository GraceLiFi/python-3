import csv
from pprint import pprint
import os
def find_total_visits():
    count = 0
    directory = 'C:\\Users\\f9hud0c\\tedprojects\\python-3\\files'
    for filename in os.listdir(directory):
        if filename.startswith("week"):
            with open(os.path.join(directory, filename)) as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    stripped = line.strip()
                    lineArr = stripped.split(", ")
                    for word in lineArr:
                        if word == "1":
                            count = count + 1
    return count

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()