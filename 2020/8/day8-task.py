
# with open("2020/8/day8testdata.txt") as f:
with open("2020/8/day8instructions.txt") as f:
    instructions = f.read().splitlines()

def run_instructions(instructions):
    stack = []
    acc = 0
    loc = 0
    pc = 0
    crashed = False

    halt = False
    while not halt:
        # has this instruction been run before?
        if loc in stack:
            halt = True
            crashed = True
        # have I got to the end
        elif loc == len(instructions):
            halt = True
        else:
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
        pc += 1

    return(crashed, acc)

# lets brute force this!
for i in range(len(instructions)):
    op = instructions[i][:3]
    if op == "nop" or op == "jmp":
        instructions_to_run = instructions.copy()
        instructions_to_run[i] = ("jmp" if op == "nop" else "nop") + instructions[i][3:]
        crashed, acc = run_instructions(instructions_to_run)
        # print(crashed, acc)
        if crashed == False:
            print(acc)
