import sys
#[seeds,map,map,map]

#map: [[srcStart,srcEnd,dstStart,dstEnd],[...]]

def parseMaps(fData):
  chunks = fData.split('\n\n')
  seeds = chunks[0].split()
  seeds = seeds[1:]
  seeds = list(map(int,seeds))
  chunks = chunks[1:]
  maps = [seeds]
  for chunk in chunks:
    myMap = []
    for line in chunk.splitlines()[1:]:
      numbs = list(map(int,line.split()))
      srcStart = numbs[1]
      srcEnd = numbs[1]+numbs[2]-1

      dstStart = numbs[0]
      dstEnd = numbs[0]+numbs[2]-1

      myMap.append([srcStart,srcEnd,dstStart,dstEnd])
    maps.append(myMap)

  return maps

with open('./day5/input.txt', 'r') as file:
  filedata = file.read()

minLoc = sys.maxsize
maps = parseMaps(filedata)
for seed in maps[0]:
  val = seed
  for myMap in maps[1:]:
    for r in myMap:
      if val >= r[0] and val<=r[1]:
        val = r[2] + (val-r[0])
        break
  if val<minLoc:
    minLoc = val
print(minLoc)
