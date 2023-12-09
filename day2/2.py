numRed = 12
numGreen = 13
numBlue = 14

def parseGames(fData):
    games = []
    for line in filedata.splitlines():
        game = {}
        rounds = []
        roundStrs = line.split(';')
        firstRnd = roundStrs[0].split()
        game['id'] = int(firstRnd[1][:len(firstRnd[1])-1])

        roundStrs[0] = roundStrs[0][roundStrs[0].find(':')+1:]

        for roundStr in roundStrs:
          rnd = {
            "red": 0,
            "green": 0,
            "blue": 0
          }
          roundStr = roundStr.replace(',','')
          split = roundStr.split()
          for i in range(len(split)):
            if (i%2) == 1:
               continue
            val = int(split[i])
            color = split[i+1]
            rnd[color] = val
            i += 1
          rounds.append(rnd)
        
        game["rounds"] = rounds;

        games.append(game)
    return games

with open('./day2/input.txt', 'r') as file:
  filedata = file.read()

games = parseGames(filedata)
powerSum = 0
for game in games:
  maxRed = 0
  maxBlue = 0
  maxGreen = 0
  for round in game["rounds"]:
     if round["red"] > maxRed:
      maxRed = round["red"]
     if round["blue"] > maxBlue:
      maxBlue = round["blue"]
     if round["green"] > maxGreen:
      maxGreen = round["green"]
  powerSum+=maxRed*maxBlue*maxGreen


   
print(powerSum)
