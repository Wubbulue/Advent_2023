def parseInput(fData):
    lines = fData.splitlines()
    lines[0] = lines[0].replace(' ','')
    lines[1] = lines[1].replace(' ','')

    time = int(lines[0][5:])
    dist = int(lines[1][9:])

    return [time,dist]


with open('./day6/input.txt', 'r') as file:
  filedata = file.read()

data = parseInput(filedata)
numWins = 0
time = data[0]
distance = data[1]
for t in range(time):
    timeToMove = time-t
    distMoved = timeToMove*t
    if distMoved>distance:
        numWins += 1
print(numWins)