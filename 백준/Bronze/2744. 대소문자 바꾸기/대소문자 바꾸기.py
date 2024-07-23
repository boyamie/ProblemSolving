import sys
input = sys.stdin.readline
st = input()
ans = ''
for i in st:
    if i.isupper()==True:
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)