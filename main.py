import subprocess
import logic.utils as utils


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
    def get_last_draw():
        """Get last draw in json format"""

        def get_name_of_last_draw():

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
            return " ".join(args[10:])

        filename = get_name_of_last_draw()
        if not filename:
            return None

        path = utils.DATA_PATH + filename
        return utils.draw_to_json(utils.read_csv(path))

    @staticmethod
    def main():
        """Return json of Draw"""
        draw = Draw.get_last_draw()
        if draw:
            return draw

        # si no hay sorteos, generamos uno:
        groups_draw = Draw.run_the_draw()
        utils.to_csv(groups_draw)
        return utils.draw_to_json(groups_draw)


if __name__ == "__main__":
    # Draw.main()

    groups_draw = Draw.run_the_draw()
    Draw.print_the_draw(groups_draw)
    utils.to_csv(groups_draw)
