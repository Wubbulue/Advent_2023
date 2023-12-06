import re
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
        rnd = {
           "red": 0,
           "green": 0,
           "blue": 0
        }
        game['id'] = int(firstRnd[1][:len(firstRnd[1])-1])

        roundStrs[0] = roundStrs[roundStrs[0].find(':'):]

        for roundStr in roundStrs:
           split = roundStr.split()
           for i in range(len(split)):
              val = int(split[i])
              color = split[i+1]
              i += 1

        games.append(game)
    return games

with open('./day2/input.txt', 'r') as file:
  filedata = file.read()

games = parseGames(filedata)
print(games)
