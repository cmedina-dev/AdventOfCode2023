def part_one():
    file = open('./input.txt')
    sums = []

    for line in file.readlines():
        diffs = [int(l) for l in line.split()]
        diff_sum = []
        diff_sum.append(diffs[-1])
        while any([diff != 0 for diff in diffs]):
            diffs_temp = []
            for i in range(len(diffs) - 1, 0, -1):
                diffs_temp.append(diffs[i] - diffs[i - 1])
            diffs_temp.reverse()
            diff_sum.append(diffs_temp[-1])
            diffs = diffs_temp
        sums.append(sum(diff_sum))
    print(sum(sums))

def part_two():
    file = open('./input.txt')
    sums = []

    for line in file.readlines():
        diffs = [int(l) for l in line.split()]
        diff_sum = []
        diff_sum.append(diffs[0])
        while any([diff != 0 for diff in diffs]):
            diffs_temp = []
            for i in range(0, len(diffs) - 1):
                diffs_temp.append(diffs[i] - diffs[i + 1])
            diff_sum.append(diffs_temp[0])
            diffs = diffs_temp
        print(diffs)
        sums.append(sum(diff_sum))
    print(sum(sums))

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()
