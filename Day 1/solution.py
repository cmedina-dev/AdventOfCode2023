import re
import sys

file = open('./Day 1/input.txt')
total = 0
nums = {"one": "o1e", "two": "t2o", "three": "t3e",
        "four": "f4r", "five": "f5e", "six": "s6x",
        "seven": "s7n", "eight": "e8t", "nine": "n9e"}
numbers_only = re.compile("[^0-9]")
for line in file:
    for key in nums:
        if key in line:
            line = re.sub(key, nums[key], line)
    line = numbers_only.sub("", line)
    total += int(line[0] + line[-1])

sys.stdout.write(str(total))