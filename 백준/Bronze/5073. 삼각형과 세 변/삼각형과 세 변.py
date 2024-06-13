while 1:
    x, y, z = map(int, input().split())
    if x==y==z==0:
        break
    elif x == y == z:
        print("Equilateral")
    elif sorted([x,y,z])[2] >= sorted([x,y,z])[0]+sorted([x,y,z])[1]:
        print("Invalid")
    elif x == y or x == z or y == z:
        print("Isosceles")
    else:
        print("Scalene")  