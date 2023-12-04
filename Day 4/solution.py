import sys
file = open("input.txt")

def part_one():
    winning_total = 0

    for line in file.readlines():
        numbers = line.split(':')[1].strip()
        winning_numbers = numbers.split('|')[0]
        winning_numbers = winning_numbers.strip().split()
        possible_numbers = numbers.split('|')[1]
        possible_numbers = possible_numbers.strip().split()
        winning_sum = 0
        for number in possible_numbers:
            if number in winning_numbers:
                if winning_sum == 0:
                    winning_sum += 1
                else:
                    winning_sum *= 2
        winning_total += winning_sum

    print(winning_total)

def part_two():
    card_list = {}
    line_list = [line for line in file.readlines()]
    for line in line_list:
        card = line.split(':')[0].strip()
        card = ' '.join(card.split())
        card_list[card] = 1

    card_idx = 1
    for line in line_list:
        numbers = line.split(':')[1].strip()
        winning_numbers = numbers.split('|')[0]
        winning_numbers = winning_numbers.strip().split()
        possible_numbers = numbers.split('|')[1]
        possible_numbers = possible_numbers.strip().split()

        copy_card_idx = card_idx + 1
        for number in possible_numbers:
            if number in winning_numbers:
                card_list[f'Card {copy_card_idx}'] += 1 * card_list[f'Card {card_idx}']
                copy_card_idx += 1
        
        card_idx += 1
    total_sum = 0
    for key in card_list:
        total_sum += card_list[key]
    print(total_sum)

part_two()