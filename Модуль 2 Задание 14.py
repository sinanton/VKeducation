import sys

start, stop, step = map(int, sys.stdin.readline().split())
print(*map(lambda x: x**2 if x % 2 != 0 else -x, range(start, stop, step)), sep='\n')