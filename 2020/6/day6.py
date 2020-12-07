# open data, split into groups
# with open("2020/day6testdata.txt") as f:
with open("2020/day6answers.txt") as f:
    groups = f.read().split("\n\n")

# print(groups)

# remove \n 's, duplicates, and convert to list
for i in range(len(groups)):
    groups[i] = groups[i].replace("\n", "")
    groups[i] = list(dict.fromkeys(groups[i]))

# print(groups)

# count them up
sum_of_counts = 0
for group in groups:
    sum_of_counts += len(group)

print(sum_of_counts)