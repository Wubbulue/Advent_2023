import numpy as np

def parse(fData):
    arrs = []
    for line in fData.splitlines():
        arrs.append(list(map(int,line.split())))
    return arrs

with open('./day9/input.txt', 'r') as file:
    filedata = file.read()

arrs = parse(filedata)
arrs = np.array(arrs)
sum = 0
for arr in arrs:
    diffs = [np.diff(arr)]
    while diffs[-1].any():
        diffs.append(np.diff(diffs[-1]))
    extrap = 0
    for diff in reversed(diffs):
        extrap=diff[0]-extrap
    extrap-=arr[0]  
    sum-=extrap
print(sum)
