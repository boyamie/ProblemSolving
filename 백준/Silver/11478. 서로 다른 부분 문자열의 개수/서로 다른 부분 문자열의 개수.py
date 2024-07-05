s = input()
n=len(s)
ans = []
for i in range(n):
    for j in range(i+1,n+1):
        ans.append(s[i:j])
print(len(list(set(ans))))