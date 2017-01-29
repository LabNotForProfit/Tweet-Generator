import sys

t = int(raw_input().strip())

for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    on_time = 0

    for time in a:
        if time <= 0:
            on_time += 1

    if on_time < k:
        print("YES")
    else:
        print("NO")
