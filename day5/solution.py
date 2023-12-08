import multiprocessing
import time
from collections import OrderedDict

file = open("./day5/input.txt")
seeds = file.readline().split(':')[1].strip().split()
seeds_part_two = [int(seed) for seed in seeds]
valid_ranges = []
range_ptr = 1
for i in range(0, len(seeds_part_two), 2):
    valid_ranges.append([seeds_part_two[i], seeds_part_two[i] + seeds_part_two[range_ptr]])
    range_ptr += 2

class HashTable:
    def __init__(self):
        self.table = OrderedDict()

    def add(self, id):
        self.table[id] = True

    def get_head(self):
        return next(iter(self.table), None)
    
    def get_tail(self):
        return next(reversed(self.table), None) if self.table else None

    def print_table(self):
        for id in self.table:
            print(id, end=" -> ")
        print("None")

def get_root(seed):
    ht = HashTable()
    ht.add(int(seed))
    return ht

def get_next_input(key1, key2):
    line = file.readline()
    while key1 not in line and key2 not in line:
        line = file.readline()

def get_range():
    ranges = []
    range = file.readline().strip()
    ranges.append(range)
    while range != "":
        range = file.readline().strip()
        ranges.append(range)
    return [[int(r) for r in range.split()] for range in ranges if len(range) > 0]

def update_path(path, path_tail, ranges):
    offsets = []
    bounds = []
    for range in ranges:
        offsets.append(range[0] - range[1])
        bounds.append([range[0], range[0] + range[2]])

    in_bound = False
    for idx, bound in enumerate(bounds):
        if path_tail >= bound[0] and path_tail < bound[1]:
            in_bound = True
        if in_bound:
            path.add(path_tail - offsets[idx])
            break
    if not in_bound:
        path.add(path_tail)

def process_chunk(j, chunk_size, ranges):
    for k in range(j, j + chunk_size):
        path = get_root(k)
        for r in ranges:
            update_path(path, path.get_tail(), r)
        path_tail = path.get_tail()
        for valid_range in valid_ranges:
            if path_tail >= valid_range[0] and path_tail <= valid_range[1]:
                path.print_table()
                print(f'SEED FOUND: {path_tail} loc: {path.get_head()}')
                quit()

def find_seed(ranges):
    for k in range(0, 100000000):
        path = get_root(k)
        for r in ranges:
            update_path(path, path.get_tail(), r)
        path_tail = path.get_tail()
        for valid_range in valid_ranges:
            if path_tail >= valid_range[0] and path_tail <= valid_range[1]:
                path.print_table()
                print(f'SEED FOUND: {path_tail} loc: {path.get_head()}')
                quit()

def main():
    ranges = []
    get_next_input("soil", "fertilizer")
    ranges.append(get_range())
    get_next_input("fertilizer", "water")
    ranges.append(get_range())
    get_next_input("water", "light")
    ranges.append(get_range())
    get_next_input("light", "temperature")
    ranges.append(get_range())
    get_next_input("temperature", "humidity")
    ranges.append(get_range())
    get_next_input("humidity", "location")
    ranges.append(get_range())
    get_next_input("humidity", "location")
    ranges.append(get_range())
    ranges.reverse()

    manager = multiprocessing.Manager()
    cur_min = manager.Value('i', float('inf'))
    terminate = manager.Value('b', False)
    lock = manager.Lock()
    pool = multiprocessing.Pool()

    chunk_size = 10000
    for j in range(0, 28000000, chunk_size):
            pool.apply_async(process_chunk, args=(j, chunk_size, ranges))

    pool.close()
    pool.join()
    # print(f'Min value: {cur_min.value}')

if __name__ == "__main__":
    main()
