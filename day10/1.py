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
for path in paths:
    if path:
        print(len(path)//2)

