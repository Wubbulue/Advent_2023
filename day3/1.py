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

nRows = len(mat)
nCols = len(mat[0])
sum = 0
for numRange in numRanges:
    valid = False
    row = numRange[0]
    for col in range(numRange[1],numRange[2]+1):
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i < 0 or i>=nRows or j < 0 or j >= nCols or valid:
                    continue
                if isSymbol(mat[i][j]):
                    valid = True
                    break
    if valid:
        power = 1
        for j in range(numRange[2],numRange[1]-1,-1):
            sum+=int(mat[row][j])*power
            power*=10

print(sum)






