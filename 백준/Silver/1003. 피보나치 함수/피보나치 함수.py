import sys
input = sys.stdin.readline

# DP 배열을 미리 생성 (최대 40까지 가능)
dp = [(0, 0)] * 41
dp[0] = (1, 0)  # fibonacci(0) 호출 횟수 (1, 0)
dp[1] = (0, 1)  # fibonacci(1) 호출 횟수 (0, 1)

# DP 테이블 채우기
for i in range(2, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

t = int(input())
for _ in range(t):
    x = int(input())
    print(dp[x][0], dp[x][1])  # 미리 계산된 값 출력
