def all_unique(str):
    return len(str) == len(set(str))

def is_two_pair(str):
    return len(set(str)) == 3

file = open('./input.txt')
hands = []
bets = []
for line in file.readlines():
    line = line.split()
    hands.append(line[0].strip())
    bets.append(line[1].strip())

for hand in hands:
    if hand.count(hand[0]) == 5:
        # guaranteed 5 of a kind
        break
    elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        # guaranteed 4 of a kind
        break
    elif hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
        # check full house or 3 of a kind
        break
    elif all_unique(hand):
        # guaranteed high card
        break
    elif is_two_pair(hand):
        # guaranteed two pair
        break
    else:
        # only remaining possibility is one pair
        break
