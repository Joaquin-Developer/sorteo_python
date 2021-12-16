import os
import subprocess
import datetime
from datetime import datetime
import utils as utils


class Draw():

    @staticmethod
    def run_the_draw():
        data = utils.get_data()
        groups_draw = [[] for x in data[0]]
        # Groups:
        for i in range(0, len(groups_draw)):
            # Data:
            for j in range(0, len(data)):
                index = utils.get_random_index_from_list(max=len(data[j]) - 1)
                groups_draw[i].append(data[j][index])
                # remove raffled team in bombo:
                data[j].pop(index)

        return groups_draw


    @staticmethod
    def print_the_draw(groups_draw):
        groups_letters = utils.get_groups_letters(groups_draw)

        print("========================================")
        for i in range(0, len(groups_letters)):
            print(f"GRUPO {groups_letters[i]}")
            for group in groups_draw[i]:
                print(f"- {group}")
            print("========================================")


    @staticmethod
    def main():
        # draw = Draw.get_last_draw()
        # if draw is not None: 
        #     return draw

        # si no hay sorteos hacemos uno nuevo, y luego lo retornamos:
        groups_draw = Draw.run_the_draw()
        utils.to_csv(groups_draw)
        return utils.draw_to_json(groups_draw)
        

    @staticmethod
    def get_last_draw():
        """
        obtenemos el último sorteo
        Lo retornamos en formato json
        """
        def get_name_of_last_draw():
            command = subprocess.run(["ls", "-lat", "data/"], 
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            lines = str(command.stdout, "UTF-8").split("\n")
            # eliminamos las primeras 3 lineas  y las últimas 2:
            del lines[0:3]
            del lines[-1]
            
            # si solo queda un archivo (teams.csv) o ninguno, es porque no hay sorteos.
            if len(lines) < 2: 
                return None

            # el primer elemento es el ultimo sorteo: 
            last_draw = lines[0]
            print(last_draw)
            args = last_draw.split(" ")
            # created_at = " ".join(args[10:]).replace(".csv", "")
            # created_at = datetime.strptime(created_at, "%d-%m-%Y %H:%M")
            return " ".join(args[9:])

        filename = get_name_of_last_draw()
        if filename is None:
            return None

        path = utils.DATA_PATH + filename
        # lo que sigue es obteber el archivo desde su nombre...

        print(get_name_of_last_draw())



if __name__ == "__main__":
    Draw.main()

    # groups_draw = run_the_draw()
    # print_the_draw(groups_draw)
    # utils.to_csv(groups_draw)
