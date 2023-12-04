import sys
import re

def part_one():
    file = open('./Day 2/input.txt', 'r')
    lines = file.readlines()
    id_sum = 0
    for line in lines:
        colors_line = line.split(':')[1]
        id = line.split(':')[0].split(' ')[1]
        colors_line = re.sub('[,]', '', colors_line)
        sets = colors_line.strip().split(';')
        color_threshold = True

        for set in sets:
            set = set.strip()
            colors = {"red": 0, "green": 0, "blue": 0}
            color_ptr = 1
            dice = set.split(' ')
            for i in range(0, len(dice), 2):
                colors[dice[color_ptr]] += int(dice[i])
                color_ptr += 2
            if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
                color_threshold = False
        
        if color_threshold == True:
            id_sum += int(id)
    print(id_sum)

def part_two():
    file = open('./Day 2/input.txt', 'r')
    lines = file.readlines()
    power_sum = 0
    for line in lines:
        colors_line = line.split(':')[1]
        id = line.split(':')[0].split(' ')[1]
        colors_line = re.sub('[;,]', '', colors_line)
        dice = colors_line.strip().split(' ')
        color_ptr = 1
        max_colors = {"red": 0, "blue": 0, "green": 0}
        for i in range(0, len(dice), 2):
            if int(dice[i]) > max_colors[dice[color_ptr]]:
                max_colors[dice[color_ptr]] = int(dice[i])
            color_ptr += 2
        powers = 1
        for color in max_colors:
            powers *= max_colors[color]
        power_sum += powers
    print(power_sum)

part_one()
part_two()