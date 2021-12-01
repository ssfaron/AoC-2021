# Part 1

with open('C:\\AoC-2021\\inputs\\day_1.txt') as f:
    lines = f.readlines()

depths = []

for line in lines: 
    depths.append(int(line))

status = []

for i in range(0, len(depths)-1):
    if depths[i] < depths[i+1]:
        status.append("increased")
    if depths[i] > depths[i+1]:
        status.append("decreased")

increased_count = 0
decreased_count = 0

for update in status:
    if update == "increased":
        increased_count += 1
    if update == "decreased":
        decreased_count += 1

#print(increased_count)
#print(decreased_count)
#print(increased_count + decreased_count)
#print(len(depths))

# Part 2

sums = []
sliding_status = []

for i in range(0, len(depths)-2):
    sums.append(depths[i]+depths[i+1]+depths[i+2])

for i in range(0, len(sums)-1):
    if sums[i] < sums[i+1]:
        sliding_status.append("increased")
    if sums[i] > sums[i+1]:
        sliding_status.append("decreased")
    if sums[i] == sums[i+1]:
        sliding_status.append("no change")

increased_count = 0
decreased_count = 0
static_count = 0

for update in sliding_status:
    if update == "increased":
        increased_count += 1
    if update == "decreased":
        decreased_count += 1
    if update == "no change":
        static_count += 1

print(increased_count)
print(decreased_count)
print(static_count)
print(increased_count + decreased_count + static_count)
print(len(sums))

print(sums[len(sums)-1])


    