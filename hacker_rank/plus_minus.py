import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos, negs, zeros = 0.0

for num in arr:
    if num > 0.0:
        pos += 1
    elif num < 0.0:
        negs += 1
    else:
        zeros += 1

pos = pos/n
negs = negs/n
zeros = zeros/n

print("%.6f" % round(pos,6))
print("%.6f" % round(negs,6))
print("%.6f" % round(zeros,6))
