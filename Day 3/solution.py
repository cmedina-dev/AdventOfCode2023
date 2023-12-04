import sys
import re

def main():
    file = open('./Day 3/input.txt', 'r')
    lines = file.readlines()
    grid = []
    valid_numbers = []
    hot_coordinates = {}
    symbol_coords = []
    star_coords = []
    digits = ["1","2","3","4","5","6","7","8","9","0"]

    for line in lines:
        grid.append(line.strip())

    isolator_re = re.compile("[^0-9]")
    symbols_re = re.compile("[0-9]")
    for i in range(len(grid)):
        number_counter = 0
        isolator = isolator_re.sub(".", grid[i])
        symbols = symbols_re.sub('.', grid[i])
        numbers = isolator.split('.')
        numbers = [number for number in numbers if number != '']
        start_idx = 0
        end_idx = 0
        while start_idx < len(isolator):
            if (symbols[start_idx] != '.'):
                if (symbols[start_idx] == '*'):
                    star_coords.append(f'({start_idx}, {i})')
                symbol_coords.append(f'({start_idx}, {i})')
            if isolator[start_idx] not in digits:
                start_idx += 1
            else:
                end_idx = start_idx
                while end_idx < len(isolator):
                    if isolator[end_idx] in digits:
                        end_idx += 1
                    else:
                        break
                for j in range(start_idx, end_idx):
                    add_coord(hot_coordinates, f'({j}, {i-1})', numbers[number_counter])
                    add_coord(hot_coordinates, f'({j}, {i+1})', numbers[number_counter])
                add_coord(hot_coordinates, f'({start_idx-1}, {i+1})', numbers[number_counter])
                add_coord(hot_coordinates, f'({start_idx-1}, {i-1})', numbers[number_counter])
                add_coord(hot_coordinates, f'({end_idx}, {i+1})', numbers[number_counter])
                add_coord(hot_coordinates, f'({end_idx}, {i-1})', numbers[number_counter])
                add_coord(hot_coordinates, f'({end_idx}, {i})', numbers[number_counter])
                add_coord(hot_coordinates, f'({start_idx-1}, {i})', numbers[number_counter])
                start_idx = end_idx
                number_counter += 1
                if (end_idx >= len(isolator) - 1):
                    break
    
    star_sum = 0
    for star in star_coords:
        if star in hot_coordinates:
            if (len(hot_coordinates[star]) == 2):
                star_sum += (int(hot_coordinates[star][0]) * int(hot_coordinates[star][1]))
    print(star_sum)

    for symbol in symbol_coords:
        if symbol in hot_coordinates:
            for coord in hot_coordinates[symbol]:
                valid_numbers.append(coord)

    total_sum = 0
    for number in valid_numbers:
        total_sum += int(number)

    valid_numbers.sort(key = int)
    print(total_sum)

def add_coord(hot_coordinates, coord, val):
    if not coord in hot_coordinates:
        hot_coordinates[coord] = []
        hot_coordinates[coord].append(val)
    else:
        hot_coordinates[coord].append(val)

main()