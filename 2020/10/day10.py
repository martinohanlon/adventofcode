# with open("2020/10/day10-testdata1.txt") as f:
with open("2020/10/day10-testdata2.txt") as f:
with open("2020/10/day10-jolts.txt") as f:
    jolts = f.read().splitlines()

jolts = list(map(int, jolts))

# add in thw power adapter
jolts.append(0)

jolts = sorted(jolts)

# add in the final one
jolts.append(jolts[-1] + 3)

print(jolts)

diff1 = 0
diff3 = 0
for i in range(len(jolts) - 1):
    diff = jolts[i+1] - jolts[i]
    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

print(diff1, diff3)
print("answer", diff1 * diff3)