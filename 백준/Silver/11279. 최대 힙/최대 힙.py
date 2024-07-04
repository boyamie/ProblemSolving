import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x !=0:
        hq.heappush(heap,(-x))
    else:
        try:
            print(-1 * hq.heappop(heap))
        except:
            print(0)