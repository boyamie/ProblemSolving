array = [[0] * 100 for i in range(100)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    for wi in range(a, a+10):
        for he in range(b, b+10):
            array[wi][he] = 1

color = 0

for i in range(100):
    color += array[i].count(1)
    
print(color)