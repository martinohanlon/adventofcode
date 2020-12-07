from collections import namedtuple

Password = namedtuple('Password', ['letter', 'lower', 'upper', 'password'])

with open("day2passwords.txt") as f:
    data = f.readlines()

# parse passwords
passwords = []
for line in data:
    # split out the parts
    rule = line.split(": ")[0]
    password = line.split(": ")[1].strip()
    letter = rule.split(" ")[1]
    lower = rule.split(" ")[0].split("-")[0]
    upper = rule.split(" ")[0].split("-")[1]
    
    # create a list of passwords
    passwords.append(Password(letter=letter, lower=int(lower), upper=int(upper), password=password))

# check passwords
correct_passwords = 0
for password in passwords:
    times = password.password.count(password.letter)
    if times >= password.lower and times <= password.upper:
        correct_passwords += 1
    # print(password.password, password.letter, times)

print(correct_passwords)