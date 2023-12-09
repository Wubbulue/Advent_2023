def parseInput(fData):
    lines = fData.splitlines()
    times = lines[0].split()
    times = list(map(int,times[1:]))

    distances = lines[1].split()
    distances = list(map(int,distances[1:]))

    return [times,distances]


with open('./day6/input.txt', 'r') as file:
  filedata = file.read()

data = parseInput(filedata)
numWins = [0] * len(data[0])
for i in range(len(data[0])):
   time = data[0][i]
   distance = data[1][i]
   for t in range(time):
      timeToMove = time-t
      distMoved = timeToMove*t
      if distMoved>distance:
         numWins[i] += 1
product = 1
for win in numWins:
   product*=win
print(product)