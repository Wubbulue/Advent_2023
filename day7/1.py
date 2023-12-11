from functools import cmp_to_key
labelToValue = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14,
}

def compare(item1,item2):
  for i in range(5):
    if labelToValue[item1[i]] < labelToValue[item2[i]]:
        return -1
    if labelToValue[item1[i]] > labelToValue[item2[i]]:
        return 1
  return 0

def fullCompare(i1,i2):
  item1 = i1[0]
  item2 = i2[0]
  ht1 = handType(item1)
  ht2 = handType(item2)
  if ht1 < ht2:
    return -1
  if ht1 > ht2:
    return 1
  else:
    # return 0
    return compare(item1,item2)

def handType(hand):
  countsDict = {}
  for i in range(5):
    c = hand[i]
    count = hand.count(c)
    countsDict.update({c:count})
  
  counts = list(countsDict.values())
  if 5 in counts:
    return 7
  elif 4 in counts:
    return 6
  elif 3 in counts and 2 in counts:
    return 5
  elif 3 in counts:
    return 4
  elif counts.count(2) == 2:
    return 3
  elif 2 in counts:
    return 2
  else:
    return 1

def parseHands(fData):
  hands = []
  for line in fData.splitlines():
    spl = line.split()
    hands.append([spl[0],int(spl[1])])
  return hands


with open('./day7/input.txt', 'r') as file:
  filedata = file.read()

hands = parseHands(filedata)
hands = sorted(hands,key=cmp_to_key(fullCompare),reverse = False)
rank = 1
sum = 0
for hand in hands:
    sum+=hand[1]*rank
    rank+=1

print(sum)