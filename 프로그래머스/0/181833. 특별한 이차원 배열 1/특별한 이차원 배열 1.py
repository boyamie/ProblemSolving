def solution(n):
    blk = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        blk[i][i] += 1
    return blk
