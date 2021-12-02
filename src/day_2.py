# Part 1

with open('C:\\AoC-2021\\inputs\\day_2.txt') as f:
    lines = f.readlines()

instructions = []
values = []

for line in lines: 
    instructions.append(line.split(" ", 1)[0])
    values.append(int(line.split(" ", 1)[1]))

horizontal = 0
depth = 0
aim = 0 # Part 2

for instruction, value in zip(instructions, values):
    if instruction == "forward":
        horizontal = horizontal + value
        depth = depth + (aim*value)
    if instruction == "down":
        aim = aim + value
    if instruction == "up":
        aim = aim - value

print(horizontal)
print(depth)
print(aim)
print(horizontal*depth)




