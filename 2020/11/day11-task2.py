# with open("2020/11/day11-testdata.txt") as f:
with open("2020/11/day11-seats.txt") as f:
# with open("2020/11/day11-testdata2.txt") as f:
    data = f.read().splitlines()

seats = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] != ".":
            seats[x,y] = data[y][x]

x_bound = x
y_bound = y

# print(seats)
def get_occupied_seats(seats, seat_pos):
    occupied = 0
    directions = {
        "n": (0,-1),
        "ne": (1,-1),
        "e": (1,0),
        "se": (1,1),
        "s": (0,1),
        "sw": (-1, 1),
        "w": (-1, 0),
        "nw": (-1, -1)
    }

    for direction in directions.keys():
        can_see = True
        see_pos = (seat_pos[0] + directions[direction][0], seat_pos[1] + directions[direction][1])
        while can_see:
            if see_pos[0] >= 0 and see_pos[1] >= 0 and see_pos[0] <= x_bound and see_pos[1] <= y_bound:
                # print(direction)
                # print(see_pos)
                whats_there = seats.get(see_pos, ".")
                # print(whats_there)
                if whats_there == "L":
                    can_see = False
                if whats_there == "#":
                    can_see = False
                    occupied += 1
                see_pos = (see_pos[0] + directions[direction][0], see_pos[1] + directions[direction][1])
            else:
                can_see = False

    return occupied

def print_seats(seats):
    for y in range(0, y_bound + 1):
        line = ""
        for x in range(0, x_bound + 1):
            line += seats.get((x,y), ".") 
        print(line)
    print("\n")

# print_seats(seats)
# print(get_occupied_seats(seats, (4,4)))

rounds = 0
seat_changes = -1
while seat_changes != 0:

    seat_changes = 0
    rounds += 1
    new_seats = {}
    for seat_pos in seats.keys():
        adj_occupied = get_occupied_seats(seats, seat_pos)
        if seats[seat_pos] == "L" and adj_occupied == 0:
            new_seats[seat_pos] = "#"
            seat_changes += 1
        elif seats[seat_pos] == "#" and adj_occupied >= 5:
            new_seats[seat_pos] = "L"
            seat_changes += 1
        else:
            new_seats[seat_pos] = seats[seat_pos]
    
    seats = new_seats
    # print_seats(seats)

    # if rounds == 3:
    #     break

# print(rounds)
# print(seats)

# count occupied seats
occupied_seats = 0
for seat_pos in seats.keys():
    if seats[seat_pos] == "#":
        occupied_seats += 1

print(occupied_seats)