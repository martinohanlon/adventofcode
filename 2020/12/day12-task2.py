import math

def rotate(xy, angle):
    angle = math.radians(angle)
    x, y = xy
    xx = x * math.cos(angle) + y * math.sin(angle)
    yy = -x * math.sin(angle) + y * math.cos(angle)

    return [round(xx), round(yy)]

# with open("2020/12/day12testdata.txt") as f:
with open("2020/12/day12directions.txt") as f:
    directions = f.read().splitlines()

way_point = [10, 1]
pos = [0, 0]

for direction in directions:
    instruction = direction[0]
    value = int(direction[1:])
    # print(instruction, value, way_point)
    if instruction == "F":
        pos[0] += (way_point[0] * value)
        pos[1] += (way_point[1] * value)
    elif instruction == "R":
        way_point = rotate(way_point, value)
    elif instruction == "L":
        way_point = rotate(way_point, 360 - value)
    elif instruction == "N":
        way_point[1] = way_point[1] + value
    elif instruction == "S":
        way_point[1] = way_point[1] - value
    elif instruction == "E":
        way_point[0] = way_point[0] + value
    elif instruction == "W":
        way_point[0] = way_point[0] - value
    # print(pos)

manhattan = abs(pos[0]) + abs(pos[1])
print(manhattan)