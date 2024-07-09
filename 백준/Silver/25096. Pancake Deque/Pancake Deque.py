import sys
input = sys.stdin.readline
from collections import deque

def max_paying_customers(T, test_cases):
    results = []
    for case_number in range(1, T + 1):
        N, pancakes = test_cases[case_number - 1]
        dq = deque(pancakes)
        
        max_deliciousness = -1
        paying_customers = 0
        
        while dq:
            if dq[0] <= dq[-1]:
                pancake = dq.popleft()
            else:
                pancake = dq.pop()
            
            if pancake >= max_deliciousness:
                paying_customers += 1
                max_deliciousness = pancake
        
        results.append(f"Case #{case_number}: {paying_customers}")
    
    return results

t = int(input().strip())
test_cases = []

for _ in range(t):
    n = int(input().strip())
    pancakes = list(map(int, input().strip().split()))
    test_cases.append((n, pancakes))

results = max_paying_customers(t, test_cases)
for result in results:
    print(result)
