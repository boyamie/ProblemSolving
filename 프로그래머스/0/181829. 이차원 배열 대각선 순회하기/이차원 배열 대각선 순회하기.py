def solution(board, k):
    ans =[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if int(i)+int(j) <= k:
                ans.append(board[i][j])
    return sum(ans)