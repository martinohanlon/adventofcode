with open("day1numbers.txt") as f:
    numbers = f.readlines()

answer = None

numbers_2 = numbers.copy()
numbers_3 = numbers.copy()
for number1 in numbers:
    for number2 in numbers_2:
        if int(number1.strip()) + int(number2.strip()) == 2020:
            answer = int(number1.strip()) * int(number2.strip())

print(answer)
