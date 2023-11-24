from ValidationException import ValidationException
import re

def validate_file(fileInput):
    lines = []
    with open(fileInput, "r") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            lines.append(line)
    lines = lines[1:]
    stripped = [line.strip() for line in lines]
    removedId = [re.sub(r'\d+,\s', '', line) for line in stripped]
    for ele in removedId:
        try:
            int(ele)
        except ValueError:
            raise ValidationException("Invalid mileage: " + ele)



def ex1():
    try:
        validate_file("C:\\Users\\f9hud0c\\tedprojects\\python-3\\files\\input.txt")
    except ValidationException as ve:
        print(ve)

ex1()