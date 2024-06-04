import subprocess
import argparse
import random
from datetime import datetime
from typing import List, Dict, Any
import logic.utils as utils


class Draw:
    generate_new_sorteo: bool = False
    generate_new_bombo: bool = False
    metadata_path: str = None

    metadata: Dict[str, Any]
    all_teams_metadata: List[str]
    cant_bombos: int = None
    cant_teams_x_bombo: int = None
    bombos_list: List[List[str]]

    @classmethod
    def generate(cls) -> Dict[str, List[str]]:
        print("- Generating Sorteo")

        groups = {chr(65 + i): [] for i in range(cls.cant_teams_x_bombo)}

        for _ in range(cls.cant_teams_x_bombo):
            for bombo in cls.bombos_list:
                team = random.choice(bombo)
                bombo.remove(team)
                groups[chr(65 + _)].append(team)

        cls.save_draw(groups)
        cls.print_result(groups)
        return groups

    @classmethod
    def save_draw(cls, groups: Dict[str, List[str]]):
        print("- Persisting groups json data")
        today = datetime.now()
        filename = f"{utils.DATA_PATH}SORTEO {today.strftime('%d-%m-%Y %H:%M')}.json"
        utils.save_json(groups, filename)

    @classmethod
    def print_result(cls, groups: Dict[str, List[str]]):
        """
        Print Sorteo in console
        """
        print("========================================")
        for key, value in groups.items():
            print(f"GRUPO {key}")
            for group in value:
                print(f"- {group}")
            print("========================================")

    @classmethod
    def get_last_draw(cls) -> Dict[str, Dict[str, str]]:
        """Get last draw in json format"""
        print("- Get last Draw")

        command = subprocess.run(
            ["ls", "-lat", "data/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        lines = str(command.stdout, "UTF-8").split("\n")
        filenames = list(filter(lambda x: "SORTEO" in x, lines))

        # si no hay archivos, es porque no hay sorteos.
        if len(filenames) == 0:
            return None

        # el primer elemento es el ultimo sorteo:
        name_last_draw = filenames[0]
        args = name_last_draw.split(" ")
        # created_at = " ".join(args[10:]).replace(".csv", "")
        # created_at = datetime.strptime(created_at, "%d-%m-%Y %H:%M")
        filename = " ".join(args[10:])

        return utils.read_json(utils.DATA_PATH + filename)

    @classmethod
    def generate_bombo(cls) -> List[str]:
        """
        A partir de la lista de equipos define los bombos.
        """
        print("- Generating bombo data")

        bombos = []
        max_teams = len(cls.all_teams_metadata)

        if cls.cant_bombos * cls.cant_teams_x_bombo != max_teams:
            raise ValueError("La cantidad de equipos no coincide con la distribución de bombos")

        index_list = [i for i in range(max_teams)]
        utils.shuffle(index_list)

        for i in range(cls.cant_bombos):
            bombo = [
                cls.all_teams_metadata[index_list[j]]
                for j in range(i * cls.cant_teams_x_bombo, (i + 1) * cls.cant_teams_x_bombo)
            ]
            print(f"Bombo {i + 1}:")
            for team in bombo:
                print(f"- {team}")

            bombos.append(bombo)

        print("**********************\n\n\n")
        cls.save_bombo(bombos)
        return bombos

    @classmethod
    def save_bombo(cls, bombo: List[str]):
        cls.bombos_list = bombo
        utils.save_json(bombo, "data/bombo.json")

    @classmethod
    def load_metadata(cls):
        if not cls.metadata:
            path = cls.metadata_path or "data/teams_metadata.json"
            cls.metadata = utils.read_json(path)

        cls.all_teams_metadata = cls.metadata["teams"]
        cls.cant_bombos = cls.metadata["metadata"]["cant_bombos"]
        cls.cant_teams_x_bombo = cls.metadata["metadata"]["cant_teams_x_bombo"]

    @classmethod
    def _main(cls) -> Dict[str, List[str]]:
        cls.load_metadata()

        if cls.generate_new_bombo:
            cls.generate_bombo()

        if cls.generate_new_sorteo:
            return cls.generate()
        return cls.get_last_draw()

    @classmethod
    def main(
        cls,
        generate_new: bool = False,
        generate_bombo: bool = False,
        metadata_path: str = None,
        metadata_info: Dict[str, Any] = None
    ):
        cls.generate_new_bombo = generate_bombo
        cls.generate_new_sorteo = generate_new
        cls.metadata_path = metadata_path
        cls.metadata = metadata_info

        return cls._main()


def get_args() -> Dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-gb", "--generate-bombo", dest="generate_bombo", action="store_true")
    parser.add_argument("-n", "--generate-new", dest="generate_new", action="store_true")
    parser.add_argument("-p", "--path", dest="metadata_path", required=True, type=str)
    return vars(parser.parse_args())


def main():
    args = get_args()
    Draw.main(
        args["generate_bombo"],
        args["generate_new"],
        args["metadata_path"]
    )


if __name__ == "__main__":
    main()
