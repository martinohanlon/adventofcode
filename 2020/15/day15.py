# numbers = [0,3,6]
# numbers = [1,3,2]
# numbers = [2,1,3]
numbers = [0,14,1,3,7,9]

rounds = 2020

def listrindex(li, number):
    try:
        return len(li) - 1 - li[::-1].index(number)
    except ValueError:
        return None

def get_last_2_indexes(li, number):
    # get all indexes of when the number has been spoken
    indices = [i for i, x in enumerate(li) if x == number]
    return indices[-2:]

for i in range(len(numbers)-1, rounds - 1):
    # print(numbers)
    # how many times spoken?
    last_number = numbers[i]
    times = numbers.count(last_number)
    if times > 1:
        last_2_indexes = get_last_2_indexes(numbers, last_number)
        # print(last_2_indexes)
        numbers.append((last_2_indexes[1] + 1) - (last_2_indexes[0] + 1))
    else:
        numbers.append(0)
    
# print(listrindex(numbers, 6))
# print(listrindex(numbers, 5))
print(len(numbers))
print(numbers[-1])