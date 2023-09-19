
with open("2022day6.txt", "r") as input:
    data = input.read()

############# Part 1 ################
answer1 = -1
marker = data[:4]
newData = data[4:]
for str in newData:
    if len(marker) == len(set(marker)):
        answer1 = data.index(marker) + 4
        break

    marker = marker[1:] + str

print(answer1)

############# Part 2 ###############
answer2 = -1
marker = data[:14]
newData = data[14:]
for str in newData:
    if len(marker) == len(set(marker)):
        answer2 = data.index(marker) + 14
        break

    marker = marker[1:] + str

print(answer2)
