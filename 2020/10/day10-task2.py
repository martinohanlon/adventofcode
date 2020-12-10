# with open("2020/10/day10-testdata1.txt") as f:
# with open("2020/10/day10-testdata2.txt") as f:
with open("2020/10/day10-jolts.txt") as f:
    jolts = f.read().splitlines()

jolts = list(map(int, jolts))

# add in the power adapter
jolts.append(0)

jolts = sorted(jolts)

# add in the final one
jolts.append(jolts[-1] + 3)

paths = {}

# add the first path
paths[0] = 1

for i in jolts[1:]:
    a = paths[i-1] if i-1 in paths.keys() else 0
    b = paths[i-2] if i-2 in paths.keys() else 0
    c = paths[i-3] if i-3 in paths.keys() else 0
    paths[i] = a + b + c

the_path = max(paths.keys())
no_of_paths = paths[the_path]
print(no_of_paths)
