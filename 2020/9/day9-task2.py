# NUMBER_TO_FIND = 127
# with open("2020/9/day9testdata.txt") as f:

NUMBER_TO_FIND = 1124361034
with open("2020/9/day9numbers.txt") as f:
    raw_numbers = f.read().splitlines()

# create a new list of ints
numbers = []
for raw_number in raw_numbers:
    numbers.append(int(raw_number))

for start in range(len(numbers)):
    for stop in range(start + 2, len(numbers)):
        # print(numbers[start:stop])
        # total = int(numbers[start])
        total = 0
        for number in numbers[start:stop]:
            total += number
        if total == NUMBER_TO_FIND:
            print("found it = ", numbers[start:stop])
            weakness = min(numbers[start:stop]) + max(numbers[start:stop])
            print("encryption weakness = ", weakness)
        if total > NUMBER_TO_FIND:
            break