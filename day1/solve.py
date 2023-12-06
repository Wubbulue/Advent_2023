with open('input.txt') as file:
    sum = 0
    for line in file:
        digits = []
        for charS in line:
            char = ord(charS)

            if char >= 48 and char <= 57:
                digits.append(char)
        
        sum += (digits[0]-48)*10
        sum += digits[-1]-48
    print(sum)