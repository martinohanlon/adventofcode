with open("day1numbers.txt") as f:
    numbers = f.readlines()

answer = None

numbers_2 = numbers.copy()
numbers_3 = numbers.copy()
for number1 in numbers:
    for number2 in numbers_2:
        for number3 in numbers_3:
            if int(number1.strip()) + int(number2.strip()) + int(number3.strip()) == 2020:
                print(number1 + number2 + number3)
                answer = int(number1.strip()) * int(number2.strip()) * int(number3.strip())

print(answer)
            

