t_an = []
for i in range(3):
    t_an.append(int(input()))

if sum(t_an) != 180:
    print('Error')    
elif t_an[0] == t_an[1] == t_an[2] == 60:
    print('Equilateral')   
elif t_an[0] == t_an[1] or t_an[1] == t_an[2] or t_an[0] == t_an[2]:
    print('Isosceles')
else:
    print('Scalene')  