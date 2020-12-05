seat_code = "BBFFBBFRLL"

def get_seat(seat_code):

    row_bounds = [0,127]
    col_bounds = [0,7]
    for char in seat_code[:7]:
        # print("row_bounds = {}".format(row_bounds))
        if char == "F":
            row_bounds[1] = int(row_bounds[1] - ((row_bounds[1] - row_bounds[0]) / 2))
        else:
            row_bounds[0] = int(row_bounds[0] + ((row_bounds[1] - row_bounds[0]) / 2) + 1)

    if seat_code[7] == "F":
        row = row_bounds[0]
    else:
        row = row_bounds[0]
    # print(row)

    for char in seat_code[7:9]:
        # print("col_bounds = {}".format(col_bounds))
        
        if char == "L":
            col_bounds[1] = int(col_bounds[1] - ((col_bounds[1] - col_bounds[0]) / 2))
        else:
            col_bounds[0] = int(col_bounds[0] + ((col_bounds[1] - col_bounds[0]) / 2) + 1)

    if seat_code[9] == "L":
        col = col_bounds[0]
    else:
        col = col_bounds[1]
    # print(col)

    seat_id = (row * 8) + col
    # print(seat_id)

    return seat_id, row, col

# print(get_seat(seat_code))

with open("2020/day5seats.txt") as f:
    seat_codes = f.read().splitlines() 

highest_seat_id = 0
for seat_code in seat_codes:
    seat_id, row, col = get_seat(seat_code)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)