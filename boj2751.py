import heapq
import sys


def heap_sort(items):
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))]

l = []
N = int(sys.stdin.readline())
for i in range(N):
    l.append(int(sys.stdin.readline()))

heap_sort(l)
for i in l:
    print(i)