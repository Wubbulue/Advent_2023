# Read in the file
with open('input.txt', 'r') as file:
  filedata = file.read()

# # Replace the target string
# filedata = filedata.replace('one', '1')
# filedata = filedata.replace('two', '2')
# filedata = filedata.replace('three', '3')
# filedata = filedata.replace('four', '4')
# filedata = filedata.replace('five', '5')
# filedata = filedata.replace('six', '6')
# filedata = filedata.replace('seven', '7')
# filedata = filedata.replace('eight', '8')
# filedata = filedata.replace('nine', '9')

digits = {
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9
}

nums = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}



sum = 0
for line in filedata.splitlines():
    findPos = []
    for numKey in nums:
        found = 0
        start = 0
        while found != -1:
            found = line.find(numKey,start)
            if found!=-1:
                start = found+1
                findPos.append([nums[numKey],found])

    for numKey in digits:
        found = 0
        start = 0
        while found != -1:
            found = line.find(numKey,start)
            if found!=-1:
                start = found+1
                findPos.append([digits[numKey],found])
    findPos.sort(key=lambda item: item[1])
    sum+=findPos[0][0]*10
    sum+=findPos[-1][0]
print(sum)
            


