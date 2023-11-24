from pprint import pprint

def build_car_list():
    car_list = []
    with open('C:\\Users\\f9hud0c\\tedprojects\\python-3\\files\\input.txt') as file1, open('C:\\Users\\f9hud0c\\tedprojects\\python-3\\files\\car-ids.txt') as file2:
        file1.readline()
        while True:
            line1 = file1.readline()
            line2 = file2.readline()
            if not line1 or not line2:
                break
            stripLine1 = line1.strip()
            stripLine2 = line2.strip()
            if stripLine1.split(", ")[1].isdigit():
                newDict = {'id': int(stripLine2.split(', ')[0]), 'miles': int(stripLine1.split(", ")[1]), 'model': stripLine2.split(', ')[1]}
                car_list.append(newDict)
    print(car_list)

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
