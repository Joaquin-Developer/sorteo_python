from os import replace
import utils as utils

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

def print_the_draw(groups_draw):
    groups_letters = list(map(chr, range(65, 65 + len(groups_draw))))

    print("========================================")
    for i in range(0, len(groups_letters)):
        print(f"GRUPO {groups_letters[i]}")
        for group in groups_draw[i]:
            print(f"- {group}")
        print("========================================")


if __name__ == "__main__":
    groups_draw = run_the_draw()
    print_the_draw(groups_draw)
    utils.to_csv(groups_draw)
