from collections import namedtuple

Path = namedtuple('Path', ['right', 'down'])

paths = [
    Path(1,1),
    Path(3,1),
    Path(5,1),
    Path(7,1),
    Path(1,2)
]

def is_tree(data, line_number, position):
    # get the line
    line = data[line_number]
    # get the position
    position = position % len(line)

    return line[position] == "#"

with open("2020/day3trees.txt") as f:
    data = f.read().splitlines() 

total_trees = []
for path in paths:
    number_of_trees = 0
    position = path.right
    line_number = path.down

    while line_number < len(data):

        if is_tree(data, line_number, position):
            number_of_trees += 1
        position += path.right
        line_number += path.down

    print(number_of_trees)
    total_trees.append(number_of_trees)

answer = total_trees[0]
for trees in total_trees[1:]:
    answer = answer * trees
print(answer)