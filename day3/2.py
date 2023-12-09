def isSymbol(char):
    return (not char.isdigit()) and (char != '.')


with open('./day3/input.txt', 'r') as f:
    mat = [[item for item in line] for line in f]

for i in range(len(mat)):
    mat[i].pop()

#[row,startCol,endCol]
numRanges = []
for i in range(len(mat)):
    row = mat[i]
    startCol = -1
    endCol = -1
    for j in range(len(row)):
        char = row[j]
        if char.isdigit():
            if startCol==-1:
                startCol=j
                endCol = j
            else:
                endCol=j
        elif startCol!=-1 and endCol != -1:
            numRanges.append([i,startCol,endCol])
            startCol=-1
            endCol=-1
    if startCol!=-1 and endCol != -1:
        numRanges.append([i,startCol,endCol])

#[row,col]
gears = []
for i in range(len(mat)):
    row = mat[i]
    for j in range(len(row)):
        if mat[i][j] =='*':
            gears.append([i,j])


nRows = len(mat)
nCols = len(mat[0])
sum = 0
for gear in gears:
    #This is a python set
    indNumRanges = set()
    for i in range(gear[0]-1,gear[0]+2):
        for j in range(gear[1]-1,gear[1]+2):
            if i < 0 or i>=nRows or j < 0 or j >= nCols:
                continue
            for nrI in range(len(numRanges)):
                numRange = numRanges[nrI]
                if i==numRange[0] and j>=numRange[1] and j <= numRange[2]:
                    indNumRanges.add(nrI)
    
    if len(indNumRanges)==2:
        nums = []
        for nrI in indNumRanges:
            numRange = numRanges[nrI]
            num = 0
            power = 1
            for j in range(numRange[2],numRange[1]-1,-1):
                num+=int(mat[numRange[0]][j])*power
                power*=10
            nums.append(num)

        sum+=nums[0]*nums[1]





print(sum)






