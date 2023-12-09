import re
input = open("input.txt", "r")
lines = input.readlines()
sum = 0
valid_digits = {
    "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
    "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
for line in lines:
    for number in valid_digits:
        if number in line:
            line = re.sub(number, valid_digits[number], line)
    line = re.sub("[^0-9]", "", line)

    if(len(line) == 1):
        sum += int(line[0] + line[0])
    else:
        sum +=  int(line[0] + line[-1])
print(sum)