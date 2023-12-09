slotData = None

def recurseSlot(i):
    numWin = 0
    for num in slotData[i][1]:
        if num in slotData[i][0]:
            numWin+=1
    sum = 0
    for j in range(i+1,i+1+numWin):
        sum+=recurseSlot(j)
    return sum+1



def parseSlots(filedata):
    slotData = []
    for line in filedata.splitlines():
        spl = line.split('|')
        test = spl[0].split()[2:]
        winningList = list(map(int,spl[0].split()[2:]))
        winningSet = set(winningList)

        numbList = list(map(int,spl[1].split()))
        numbSet = set(numbList)
        slotData.append([winningSet,numbSet])
    return slotData




with open('./day4/input.txt', 'r') as file:
    filedata = file.read()

slotData = parseSlots(filedata)
sum = 0
for i in range(len(slotData)):
    sum+=recurseSlot(i)

print(sum)