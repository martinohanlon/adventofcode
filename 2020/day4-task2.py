with open("2020/day4passports.txt") as f:
    data = f.read()

# with open("2020/day4testdata.txt") as f:
#     data = f.read()

def validate_color(color):
    valid_color = True
    if color[0] != "#":
        valid_color = False
    else:
        for char in color[1:]:
            if char not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
                valid_color = False
    return valid_color

# parse data into a list of dictionaries
passports = []

raw_passports = data.split("\n\n")
for raw_passport in raw_passports:
    raw_passport = raw_passport.replace("\n", " ")
    raw_fields = raw_passport.split(" ")
    passport = {}
    for raw_field in raw_fields:
        passport[raw_field.split(":")[0]] = raw_field.split(":")[1]
    passports.append(passport)

# count the valid passports
valid_passports = 0
for passport in passports:
    if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and "cid" not in passport.keys()):

        #validate the data
        valid_passport = True
        if len(passport["byr"]) != 4 or int(passport["byr"]) < 1920 or (int(passport["byr"])) > 2002:
            valid_passport = False
            
        if len(passport["iyr"]) != 4 or int(passport["iyr"]) < 2010 or (int(passport["iyr"])) > 2020:
            valid_passport = False

        if len(passport["eyr"]) != 4 or int(passport["eyr"]) < 2020 or (int(passport["eyr"])) > 2030:
            valid_passport = False

        height = passport["hgt"][:-2]
        metric = passport["hgt"][-2:]

        if metric == "cm":
            if int(height) < 150 or int(height) > 193:
                valid_passport = False
        elif metric == "in":
            if int(height) < 59 or int(height) > 76:
                valid_passport = False
        else:
            valid_passport = False

        if not validate_color(passport["hcl"]):
            valid_passport = False

        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            valid_passport = False

        if len(passport["pid"]) != 9 or not passport["pid"].isnumeric():
            valid_passport = False

        if valid_passport:
            valid_passports += 1

print(valid_passports)