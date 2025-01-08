import sys

tc = int(sys.stdin.readline().strip())
person = []

#2차원 배열로 입력값 저장
for _ in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    person.append([a,b]) 
    #[[a1,b1], [a2,b2] ...]

for size in person: #비교대상 : person[0](55,185)
    rank = 1
    for comp in person: #비교할대상 : person[0~4](55,185 ~ 46,155)
        if size[0] < comp[0] and size[1] < comp[1]:
            rank += 1
    print(rank, end=' ')