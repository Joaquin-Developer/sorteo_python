"""utils module"""
import random
import json
from typing import List, Dict, Any

DATA_PATH = "data/"


def shuffle(_list: List[Any]) -> None:
    random.shuffle(_list)


def get_groups_letters(groups_draw) -> List[str]:
    return list(map(chr, range(65, 65 + len(groups_draw))))


def read_json(path: str) -> Dict[str, Any]:
    with open(path) as file:
        lines = file.read()
    return json.loads(lines)


def save_json(data: Any, path: str):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


class DrawNotFoundException(Exception):
    """Draw not found"""
