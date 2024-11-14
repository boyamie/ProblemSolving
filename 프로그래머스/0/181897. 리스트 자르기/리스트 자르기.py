def solution(n, slicer, num_list):
    a=slicer[0]
    b=slicer[1]
    c=slicer[2]
    if n==1:
        answer = num_list[:b+1]
    elif n==2:
        answer = num_list[a:]
    elif n==3:
        answer = num_list[a:b+1]
    else:
        answer = num_list[a:b+1:c]
    return answer