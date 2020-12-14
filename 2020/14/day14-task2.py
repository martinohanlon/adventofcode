# with open("2020/14/day14testdata.txt") as f:
# with open("2020/14/day14testdata2.txt") as f:
with open("2020/14/day14program.txt") as f:
    instructions = f.read().splitlines()

def get_locs(mask, number):
    locs = []

    # get the binary number, pad it, make it into a list
    binary_num = bin(number)[2:]
    # print("binary num =", binary_num)
    binary_num = binary_num.zfill(36)
    binary_num = list(binary_num)

    # apply the mask
    for i in range(len(mask)):
        if mask[i] == "X" or mask[i] == "1":
            binary_num[i] = mask[i]

    binary_num = "".join(binary_num)

    # sort out the Xs
    no_xs = binary_num.count("X")

    for i in range((2 ** no_xs)):
        next_loc = binary_num
        x_mask = bin(i)[2:].zfill(no_xs)
        for digit in x_mask:
            next_loc = next_loc.replace("X", digit, 1)
        locs.append(int(next_loc, 2))

    return locs

memory = {}

for instruction in instructions:
    op = instruction.split("=")[0].strip()
    arg = instruction.split("=")[1].strip()
    if op == "mask":
        mask = arg
        # print(mask)
    elif op[:3] == "mem":   
        loc = int(op[4:-1])
        for loc in get_locs(mask, loc):
            memory[loc] = int(arg)

# print(memory)
result = 0
for loc in memory.keys():
    result += memory[loc]
print(result)