# with open("2020/11/day11-testdata.txt") as f:
with open("2020/11/day11-seats.txt") as f:
    data = f.read().splitlines()

seats = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "L":
            seats[x,y] = data[y][x]

def get_occupied_seats(seats, seat_pos):
    occupied = 0

    for x in range(seat_pos[0] - 1, seat_pos[0] + 2):
        for y in range(seat_pos[1] - 1, seat_pos[1] + 2):
            adj_seat_pos = (x,y)
            if adj_seat_pos != seat_pos:
                if seats.get((x,y), ".") == "#":
                    occupied += 1

    return occupied

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
        elif seats[seat_pos] == "#" and adj_occupied >= 4:
            new_seats[seat_pos] = "L"
            seat_changes += 1
        else:
            new_seats[seat_pos] = seats[seat_pos]
    
    # print(seats)
    # print(new_seats)

    seats = new_seats

# print(rounds)
# print(seats)

# count occupied seats
occupied_seats = 0
for seat_pos in seats.keys():
    if seats[seat_pos] == "#":
        occupied_seats += 1

print(occupied_seats)