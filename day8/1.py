def parse(fData):
    maps = {}
    spl = fData.splitlines()
    steps = spl[0]
    spl = spl[2:]
    graph = {}
    for path in spl:
        source = path[0:3]
        left = path[7:10]
        right = path[12:15]
        graph.update({source:[left,right]})
    maps.update({'steps':steps})
    maps.update({'graph':graph})
    return maps



with open('./day8/test.txt', 'r') as file:
    filedata = file.read()
maps = parse(filedata)


step = 0
current = 'AAA'
numSteps = len(maps['steps'])
while current != 'ZZZ':
    move = maps['steps'][step % numSteps]
    if move == 'R':
        current = maps['graph'][current][1]
    else:
        current = maps['graph'][current][0]
    step+=1

print(step)