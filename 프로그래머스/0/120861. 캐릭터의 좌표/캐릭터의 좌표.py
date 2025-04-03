def solution(keyinput, board):
    answer = [0,0]
    w_max = int(board[0] / 2)
    h_max = int(board[1] / 2)
    for i in keyinput:
        if i == "left" and answer[0] > -w_max:
            answer[0] -= 1
        elif i == "right"and answer[0] < w_max:
            answer[0] += 1
        elif i == "up" and answer[1] < h_max:
            answer[1] += 1
        elif i == "down"and answer[1] > -h_max:
            answer[1] -= 1
    return answer