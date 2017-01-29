import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

between_sets = 0

def valid_a(current):
    for a_loop in a:
        if current % a_loop == 0:
            continue
        else:
            return False
    return True

def valid_b(current):
    for b_loop in b:
        if b_loop % current == 0:
            continue
        else:
            return False
    return True

for current in range(a[n -1], b[m - 1] + 1):
    valid = valid_a(current)
    if valid:
        also_valid = valid_b(current)
        if also_valid:
            print(current)
            between_sets += 1

print(between_sets)
