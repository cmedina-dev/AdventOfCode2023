file = open('./input.txt')
races = [int(i) for i in file.readline().split()[1:]]
distances = [int(i) for i in file.readline().split()[1:]]

total_ways = []
for i in range(len(races)):
    ways = 0
    for j in range(1, races[i]):
        if (j * (races[i] - j) > distances[i]):
            ways += 1
    total_ways.append(ways)
solution = 1
for way in total_ways:
    solution *= way
print(solution)