def is_tree(data, line_number, position):
    # get the line
    line = data[line_number]
    # get the position
    position = position % len(line)

    return line[position] == "#"

with open("2020/day3trees.txt") as f:
    data = f.read().splitlines() 

position = 0
number_of_trees = 0
for line_number in range(1,len(data)):
    position += 3
    if is_tree(data, line_number, position):
        number_of_trees += 1
    # testing :)
    #     print("hit")
    # else:
    #     print("miss")
    
    # if line_number == 3:
    #     break

print(number_of_trees)
