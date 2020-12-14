# with open("2020/14/day14testdata.txt") as f:
with open("2020/14/day14program.txt") as f:
    instructions = f.read().splitlines()

def apply_mask(mask, number):

    # get the binary number, pad it, make it into a list
    binary_num = bin(number)[2:]
    binary_num = binary_num.zfill(36)
    binary_num = list(binary_num)

    # apply the mask
    for i in range(len(mask)):
        if mask[i] != "X":
            binary_num[i] = mask[i]


    binary_num = "".join(binary_num)
    return int(binary_num, 2)


memory = {}

for instruction in instructions:
    op = instruction.split("=")[0].strip()
    arg = instruction.split("=")[1].strip()
    if op == "mask":
        mask = arg
        # print(mask)
    elif op[:3] == "mem":   
        loc = op[4:-1]
        bin_val = apply_mask(mask, int(arg))
        memory[loc] = bin_val

# print(memory)
result = 0
for loc in memory.keys():
    result += memory[loc]
print(result)