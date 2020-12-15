spoken = {}

# numbers = [0,3,6]
# numbers = [1,3,2]
# numbers = [2,1,3]
# numbers = [1,2,3]
numbers = [0,14,1,3,7,9]

# rounds = 2020
rounds = 30000000

def speak_number(number, index):
    if number in spoken.keys():
        spoken[number].append(index)
    else:
        spoken[number] = [index]

def get_next_number(number):
    if number in spoken.keys():
        last_spoken = spoken[number]
        if len(last_spoken) > 1:
            # print((last_spoken[-1] + 1), " - ", (last_spoken[-2] + 1))
            return (last_spoken[-1] + 1) - (last_spoken[-2] + 1)
        else:
            return 0
    else:
        return 0

# add the starting numbers
for i in range(len(numbers)):
    speak_number(numbers[i], i)

last_number = numbers[-1]
for i in range(len(numbers)-1, rounds - 1):
    # print(i, last_number)
    last_number = get_next_number(last_number) 
    speak_number(last_number, i+1)

# print(spoken)
print(last_number)

