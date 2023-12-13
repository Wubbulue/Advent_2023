from time import process_time

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

def isFinished(currents):
    for curr in currents:
        if curr[-1] != 'Z':
            return False
    return True



with open('./day8/input.txt', 'r') as file:
    filedata = file.read()
maps = parse(filedata)

currents = []
for src in maps['graph']:
    if src[-1] == 'A':
        currents.append(src)

currents = currents[:1]
current = 'AAA'
visits = {current:[[0,0]]}
repeat = False
step = 0
numSteps = len(maps['steps'])
while not repeat:
    localStep = step % numSteps
    move = maps['steps'][localStep]
    if move == 'R':
        current = maps['graph'][current][1]
    else:
        current = maps['graph'][current][0]
    if current in visits:
        for visit in visits[current]:
            if visit[0] == localStep:
                repeat = True
                print(f'repeat found! {current}')
                print(f'First local step: {visit[0]} global step: {visit[1]}')
                print(f'Second local step: {localStep} global step: {step}')
                break
        visits[current].append([localStep,step])
    else:
        visits.update({current:[[localStep,step]]})





# step = 0
# numSteps = len(maps['steps'])
# while not isFinished(currents):
#     move = maps['steps'][step % numSteps]

#     for i in range(len(currents)):
#         curr = currents[i]
#         if move == 'R':
#             currents[i] = maps['graph'][curr][1]
#         else:
#             currents[i] = maps['graph'][curr][0]
#     if not step % 1000000:
#         print(step)
#     step+=1

print(currents)