import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 설정

# 메모이제이션용 딕셔너리
memo = {}

# 재귀 함수 정의
def count_ways(n):
    if n == 1:
        return 1  # 1을 만드는 경우의 수: 1
    elif n == 2:
        return 2  # 2를 만드는 경우의 수: 1+1, 2
    elif n == 3:
        return 4  # 3을 만드는 경우의 수: 1+1+1, 1+2, 2+1, 3
    if n in memo:
        return memo[n]  # 이미 계산된 경우 메모에서 반환

    # 점화식 적용: f(n) = f(n-1) + f(n-2) + f(n-3)
    memo[n] = count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
    return memo[n]

# 테스트 케이스 입력
t = int(input())
for _ in range(t):
    n = int(input())
    print(count_ways(n))