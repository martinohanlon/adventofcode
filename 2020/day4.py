with open("2020/day4passports.txt") as f:
    data = f.read()

# parse data into a list of dictionaries
passports = []

raw_passports = data.split("\n\n")
# print(passports_raw)
for raw_passport in raw_passports:
    raw_passport = raw_passport.replace("\n", " ")
    raw_fields = raw_passport.split(" ")
    # print(raw_fields)
    passport = {}
    for raw_field in raw_fields:
        passport[raw_field.split(":")[0]] = raw_field.split(":")[1]
    # print(passport)
    passports.append(passport)

# count the valid passports
valid_passports = 0
for passport in passports:
    if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and "cid" not in passport.keys()):
        valid_passports += 1

print(valid_passports)