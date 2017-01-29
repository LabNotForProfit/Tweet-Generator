import sys

n = int(raw_input().strip())

for i in reversed(range(n)):
    print("%s%s" % (" " * i, "#" * (n - i)))
