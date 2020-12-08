stack = []
acc = 0
loc = 0
pc = 0

# with open("2020/8/day8testdata.txt") as f:
with open("2020/8/day8instructions.txt") as f:
    instructions = f.read().splitlines()

halt = False
while not halt:
    # has this instruction been run before?
    if loc not in stack:
        stack.append(loc)
        op = instructions[loc].split(" ")[0].strip()
        arg = instructions[loc].split(" ")[1].strip()

        if op == "acc":
            sign = arg[0]
            if sign == "+":
                acc += int(arg[1:])
            else:
                acc -= int(arg[1:])
            loc += 1

        elif op == "jmp":
            sign = arg[0]
            if sign == "+":
                loc += int(arg[1:])
            else:
                loc -= int(arg[1:])
        
        elif op == "nop":
            loc += 1
    else:
        halt = True

    pc += 1

print(acc)