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
for slot in slotData:
    numWin = 0
    for numb in slot[1]:
        if numb in slot[0]:
            numWin+=1
    
    if numWin>0:
        sum += 2**(numWin-1)

print(sum)