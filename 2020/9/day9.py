# PREAMBLE_LEN = 5
# with open("2020/9/day9testdata.txt") as f:

PREAMBLE_LEN = 25
with open("2020/9/day9numbers.txt") as f:
    numbers = f.read().splitlines()

for i in range(PREAMBLE_LEN, len(numbers)):
    preamble = numbers[i-PREAMBLE_LEN: i]
    next_number = numbers[i]
    # print(preamble)
    # print(next_number)

    valid = False
    for number1 in preamble.copy():
        for number2 in preamble.copy():
            if number1 != number2:
                if (int(number1) + int(number2) == int(next_number)):
                    valid = True

    if not valid:
        print(next_number) 
