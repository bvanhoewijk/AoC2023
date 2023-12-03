#!/usr/bin/env python3
from os import replace
import re

fh = open("input2.txt", 'r')
my_dict = dict(zip(["one", "two", "three", "four", "five", "six" , "seven", "eight", "nine"], list(range(1, 10))))

def replace_letterdigit(string):
    first = ""
    start = 10000

    for letter in ["one", "two", "three", "four", "five", "six" , "seven", "eight", "nine"]:
        p = re.compile(letter)
        for m in p.finditer(string):
            found = m.start()
            if found < start:
                start = found
                first = letter
    return first

replace_letterdigit("eightwothree")

def replace_composite(string):
    string = string.replace("oneight", "oneeight")
    string = string.replace("threeight", "threeeight")
    string = string.replace("fiveight", "fiveeight")
    string = string.replace("nineight", "nineeight")
    string = string.replace("twone", "twoone")
    string = string.replace("sevenine", "sevennine")
    string = string.replace("eightwo", "eighttwo")

    return string

s = 0
for line in fh:
    line = line.strip()

    print("==========", line)
    line = replace_composite(line)
    res = replace_letterdigit(line)
    while res:
        line = line.replace(res, str(my_dict[res]))
        res = replace_letterdigit(line)

    print(line)
    
    line = re.sub(r'\D', '', line)
    sol = int(line[0] + line[-1])
    print(sol)
    s += int(line[0] + line[-1])
    
print(f"Solution {s}")