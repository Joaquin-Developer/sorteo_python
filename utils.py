import os, datetime
import random

DATA_PATH = "data/"

def read_csv():
    path = f"{DATA_PATH}teams.csv"
    data = []
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        data.append(line.replace("\n", ""))
    
    return data

def get_data(in_json=True):
    data = read_csv()
    teams_data = []

    for elem in (data):
        teams_data.append(elem.split(":"))
    return teams_data


def to_csv(data):
    dt = datetime.datetime.now()
    path = f"{DATA_PATH}SORTEO {dt.day}-{dt.month}-{dt.year} {dt.hour}:{dt.minute}.csv"

    print(data)

    with open(path, "w") as file:
        file.write(data)

def get_random_index_from_list(max):
    return random.randint(0, max)
