import functools

def all_unique(str):
    return len(str) == len(set(str))

# 34222
# 34342

def is_two_pair(str):
    return len(set(str)) == 3

def is_full_house(str):
    return len(set(str)) == 2

def is_three_kind(str):
    return str.count(str[0]) == 3 or str.count(str[1]) == 3 or str.count(str[2]) == 3

def is_four_kind(str):
    return str.count(str[0]) == 4 or str.count(str[1]) == 4

def is_five_kind(str):
    return str.count(str[0]) == 5

def part_one():
    file = open('./input.txt')
    hands = []
    for line in file.readlines():
        line = line.split()
        hands.append((line[0].strip(), int(line[1].strip())))

    five = []
    four = []
    full = []
    three = []
    two = []
    one = []
    high = []

    card_key = {'2': 2, '3': 3, 
        '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, 
        'T': 10, 'J': 11, 'Q': 12, 
        'K': 13, 'A': 14}

    def custom_sort(x, y):
        hand_one = x[0]
        hand_two = y[0]
        for i in range(0, len(hand_one)):
            if card_key[hand_one[i]] > card_key[hand_two[i]]:
                return -1
            elif card_key[hand_one[i]] < card_key[hand_two[i]]:
                return 1
        return 0

    for hand in hands:
        if is_five_kind(hand[0]):
            five.append(hand)
        elif is_four_kind(hand[0]):
            four.append(hand)
        elif is_full_house(hand[0]):
            full.append(hand)
        elif is_three_kind(hand[0]):
            three.append(hand)
        elif all_unique(hand[0]):
            high.append(hand)
        elif is_two_pair(hand[0]):
            two.append(hand)
        else:
            one.append(hand)

    custom_sort_key = functools.cmp_to_key(custom_sort)
    deck = [five, four, full, three, two, one, high]
    for hand in deck:
        hand.sort(key = custom_sort_key)

    sorted_deck = [hand for sub_list in deck for hand in sub_list]
    solution = 0
    for i in range(len(sorted_deck)):
        solution += sorted_deck[i][1] * (len(sorted_deck) - i)
    print(solution)

def part_two():
    def all_unique(str, j_count):
        return len(str) == len(set(str)) and j_count == 0

    def is_two_pair(str, j_count):
        '''****J -> J must be 0 or 1'''
        return (len(set(str)) == 3 and j_count == 0) or (len(set(str)) == 4 and j_count == 1)

    def is_full_house(str, j_count):
        '''****J -> min. full house or three-of-a-kind guaranteed'''
        '''1122J -> 12J'''
        return ((len(set(str)) == 2 and j_count == 0) or
                (len(set(str)) == 3 and j_count == 1))

    def is_three_kind(str, j_count):
        '''****J'''
        '''24111 -> 241 | JJ412 -> J12'''
        return (((str.count(str[0]) == 3 or 
                 str.count(str[1]) == 3 or str.count(str[2]) == 3) 
                 and j_count == 0) or
                (len(set(str)) == 4 and j_count == 2) or
                (len(set(str)) == 4 and j_count == 1))

    def is_four_kind(str, j_count):
        '''**JJJ -> guaranteed min. four-of-a-kind'''
        return (((str.count(str[0]) == 4 or str.count(str[1]) == 4) and j_count == 0) or 
                (len(set(str)) == 3 and j_count == 1 and (str.count(str[0]) == 3 or str.count(str[1]) == 3 or str.count(str[2]) == 3)) or
                (len(set(str)) == 3 and j_count == 2 and (str.count(str[0]) == 2 or str.count(str[1]) == 2 or str.count(str[2]) == 2)) or
                (len(set(str)) == 3 and j_count == 3))

    def is_five_kind(str, j_count):
        '''*JJJJ -> guaranteed min. five-of-a-kind'''
        return ((str.count(str[0]) == 5) or 
                (j_count == 4) or 
                (j_count == 1 and 4 in [str.count(c) for c in set(str) if c != 'J']) or
                (j_count == 2 and 3 in [str.count(c) for c in set(str) if c != 'J']) or
                (j_count == 3 and 2 in [str.count(c) for c in set(str) if c != 'J']))
    file = open('./input.txt')
    hands = []
    for line in file.readlines():
        line = line.split()
        hands.append((line[0].strip(), int(line[1].strip())))

    five = []
    four = []
    full = []
    three = []
    two = []
    one = []
    high = []

    card_key = {'2': 2, '3': 3, 
        '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, 
        'T': 10, 'J': 1, 'Q': 12, 
        'K': 13, 'A': 14}

    def custom_sort(x, y):
        hand_one = x[0]
        hand_two = y[0]
        for i in range(0, len(hand_one)):
            if card_key[hand_one[i]] > card_key[hand_two[i]]:
                return -1
            elif card_key[hand_one[i]] < card_key[hand_two[i]]:
                return 1
        return 0

    for hand in hands:
        j_count = hand[0].count("J")
        if is_five_kind(hand[0], j_count):
            five.append(hand)
        elif is_four_kind(hand[0], j_count):
            four.append(hand)
        elif is_full_house(hand[0], j_count):
            full.append(hand)
        elif is_three_kind(hand[0], j_count):
            three.append(hand)
        elif all_unique(hand[0], j_count):
            high.append(hand)
        elif is_two_pair(hand[0], j_count):
            two.append(hand)
        else:
            one.append(hand)

    custom_sort_key = functools.cmp_to_key(custom_sort)
    deck = [five, four, full, three, two, one, high]
    for hand in deck:
        hand.sort(key = custom_sort_key)

    for d in deck:
        print([a[0] for a in d if a[0].count('J') >= 1])
    sorted_deck = [hand for sub_list in deck for hand in sub_list]
    solution = 0
    for i in range(len(sorted_deck)):
        solution += sorted_deck[i][1] * (len(sorted_deck) - i)
    print(solution)

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()