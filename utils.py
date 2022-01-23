from json import encoder
import os, datetime
import random
import json
from typing import List

DATA_PATH = "data/"


def read_csv(path=None) -> List:
    if path is None:
        path = f"{DATA_PATH}teams.csv"

    data = []
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        data.append(line.replace("\n", ""))
    
    return data


def get_data(in_json=True, data_path=None) -> List:
    data = read_csv(data_path)
    teams_data = []

    for elem in (data):
        teams_data.append(elem.split(":"))
    return teams_data


def to_csv(data) -> None:
    dt = datetime.datetime.now()
    path = f"{DATA_PATH}SORTEO {dt.strftime('%d-%m-%Y %H:%M')}.csv"

    print(data)
    csv_text = ""
    for group in data:
        teams = ":".join(str(team) for team in group)
        csv_text += teams

        if (data[len(data) - 1] != group):
            csv_text += "\n"

    with open(path, "w") as file:
        file.write(csv_text)


def get_random_index_from_list(max, min=0) -> int:
    return random.randint(min, max)


def shuffle(list: list) -> None:
    random.shuffle(list)


def get_groups_letters(groups_draw) -> List:
    return list(map(chr, range(65, 65 + len(groups_draw))))


def draw_to_json(groups_draw) -> str:
    groups_letters = get_groups_letters(groups_draw)
    list_to_json = []

    for index, elem in enumerate(groups_draw):
        group = {}
        group["group"] = "GRUPO " + groups_letters[index]
        print(elem)
        names = [x for x in elem.split(":")]

        for j, team in enumerate(names):
            group[f"team{j + 1}"] = team

        list_to_json.append(group)

    return json.dumps(list_to_json, ensure_ascii=False)

