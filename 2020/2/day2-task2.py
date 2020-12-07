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

def is_char_at_pos(text, letter, position):
    try:
        if text[position] == letter:
            return True

    except IndexError:
        pass

    return False

# check passwords
correct_passwords = 0
for password in passwords:
    if (is_char_at_pos(password.password, password.letter, password.lower-1) or is_char_at_pos(password.password, password.letter, password.upper-1)) and not ((is_char_at_pos(password.password, password.letter, password.lower-1) and is_char_at_pos(password.password, password.letter, password.upper-1))):
        correct_passwords += 1
    
print(correct_passwords)