import numpy as np
import cv2
#[[rowshift,colshift],[rowshift,colshift]]
pipeMap = {
    '|': [[1,0],[-1,0]],
    '-': [[0,1],[0,-1]],
    'L': [[-1,0],[0,1]],
    'J': [[0,-1],[-1,0]],
    '7': [[1,0],[0,-1]],
    'F': [[1,0],[0,1]],
}

def walkMazeRecur(mat,path,shift):
    currentPipe = mat[path[-1][0]][path[-1][1]]
    nextPos = [path[-1][0]+shift[0],path[-1][1]+shift[1]]
    nextPipe = mat[nextPos[0]][nextPos[1]]
    if(currentPipe=='S' and len(path)>1):
        return path
    if(currentPipe=='.'):
        return False
    if(nextPipe=='S'):
        return path
    if(nextPipe=='.'):
        return False

    shiftBackward = [-x for x in shift]
    if shiftBackward in pipeMap[nextPipe]:
        idx = pipeMap[nextPipe].index(shiftBackward)
        idx = 1 - idx
        path += [nextPos]
        return walkMazeRecur(mat,path,pipeMap[nextPipe][idx])

def walkMazeIter(mat,path,shift):
    nextPos = [path[-1][0]+shift[0],path[-1][1]+shift[1]]
    nextPipe = mat[nextPos[0]][nextPos[1]]
    while nextPipe in pipeMap:
        shiftBackward = [-x for x in shift]
        if shiftBackward in pipeMap[nextPipe]:
            idx = pipeMap[nextPipe].index(shiftBackward)
            idx = 1 - idx
            path += [nextPos]
            shift = pipeMap[nextPipe][idx]
            nextPos = [path[-1][0]+shift[0],path[-1][1]+shift[1]]
            nextPipe = mat[nextPos[0]][nextPos[1]]
        else:
            return False

    if(nextPipe=='S'):
        return path
    if(nextPipe=='.'):
        return False



def parse(fData):
    maze = {}
    mat = []
    spl = fData.splitlines()
    for row in range(len(spl)):
        rowArr = []
        line = spl[row]
        for col in range(len(line)):
            char = line[col]
            rowArr.append(char)
            if(char=='S'):
                maze.update({'start':[row,col]})
        mat.append(rowArr)
    maze.update({'mat':mat})
    return maze

with open('./day10/input.txt', 'r') as file:
    filedata = file.read()


maze = parse(filedata)
paths = []
paths.append(walkMazeIter(maze['mat'],[maze['start']],[1,0]))
paths.append(walkMazeIter(maze['mat'],[maze['start']],[-1,0]))
paths.append(walkMazeIter(maze['mat'],[maze['start']],[0,1]))
paths.append(walkMazeIter(maze['mat'],[maze['start']],[0,-1]))
p = None
for path in paths:
    if path:
        p = path
p.sort(key = lambda x: x[0])
path = []
r = p[0][0]
row = []
for point in p:
    if point[0] != r:
        if len(row)%2==1:
            row = row[:len(row)-1]
        path.append(row)
        row = [point]
        r = point[0]
    else:
        row.append(point)

im = np.zeros((140, 140), np.float32)
tilesin = 0
print('test')
for row in path:
    for point in row:
        im[point[0]][point[1]] = 255.0
for row in path:
    for i in range(len(row)):
        if i%2==1:
            continue
        startCol = row[i][1]
        endCol = row[i+1][1]
        for j in range(startCol,endCol):
            if maze['mat'][row[i][0]][j]=='.':
                tilesin+=1
                im[row[i][0]][j] = 100
print(tilesin)


cv2.imwrite('test.png',im)

