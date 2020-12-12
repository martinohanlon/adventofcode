import math

# with open("2020/12/day12testdata.txt") as f:
with open("2020/12/day12directions.txt") as f:
    directions = f.read().splitlines()

compass = {
    "N": 0,
    "E": 90,
    "S": 180,
    "W": 270
}

def get_next_pos(x,y,angle,distance):
    dy = distance*math.cos(math.radians(angle))   
    dx = distance*math.sin(math.radians(angle))   
    x = round(x + dx)                               
    y = round(y + dy)
    return x, y

x = 0
y = 0
heading = compass["E"]

for direction in directions:
    instruction = direction[0]
    value = int(direction[1:])
    # print(instruction, value)
    if instruction == "F":
        x, y = get_next_pos(x, y, heading, value)
    elif instruction == "R":
        heading = heading + value
    elif instruction == "L":
        heading = heading - value
    else:
        # it must be a compass heading
        x, y = get_next_pos(x, y, compass[instruction], value)
    # print(x, y)

manhattan = abs(x) + abs(y)
print(manhattan)