import sys
from interval import *
#[seeds,map,map,map]

#map: [[srcStart,srcEnd,dstStart,dstEnd],[...]]
#seeds: [[startSeed, endSeed],[startSeed, endSeed],[...]]

def parseMaps(fData):
  chunks = fData.split('\n\n')
  seedRng = chunks[0].split()
  seedRng = seedRng[1:]
  seedRng = list(map(int,seedRng))
  seeds = []
  for i in range(len(seedRng)):
    if i%2==0:
      seeds.append(Interval(seedRng[i],seedRng[i]+seedRng[i+1]-1))
      
  chunks = chunks[1:]
  maps = [seeds]
  for chunk in chunks:
    intervals = []
    for line in chunk.splitlines()[1:]:
      numbs = list(map(int,line.split()))
      srcStart = numbs[1]
      srcEnd = numbs[1]+numbs[2]-1
      dstStart = numbs[0]
      distance = dstStart-srcStart
      intervals.append(IntervalDist(srcStart,srcEnd,distance))

    maps.append(intervals)

  return maps

with open('./day5/input.txt', 'r') as file:
  filedata = file.read()

minLoc = sys.maxsize
maps = parseMaps(filedata)
# seedToLoc = {}
for seed in maps[0]:
  print(seed)
  oldInts = [seed]
  for intervals in maps[1:]:
    newInts = []
    for i in oldInts:
      test = srcToDstList(i,intervals)
      newInts = newInts + test
    oldInts = newInts
  for i in newInts:
    if(i.low<minLoc):
      minLoc = i.low
print(minLoc)

# minLoc = sys.maxsize
# maps = parseMaps(filedata)
# for seed in maps[0]:
#   val = seed
#   i = 0
#   for iTree in maps[1:]:
#     val = srcToDest(iTree,val)
#     i+=1
#   if val<minLoc:
#     minLoc = val
# print(minLoc)

