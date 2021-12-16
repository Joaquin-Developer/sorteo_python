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
    path = f"{DATA_PATH}SORTEO {dt.strftime('%d-%m-%Y %H:%M')}.csv"

    csv_text = ""
    for group in data:
        teams = " ".join(str(team) for team in group).replace(" ", ":")
        csv_text += teams

        if (data[len(data) - 1] != group):
            csv_text += "\n"

    with open(path, "w") as file:
        file.write(csv_text)

def get_random_index_from_list(max):
    return random.randint(0, max)

def draw_to_json(draws_group):
    pass
