n = int(input())
total = 1
count = 1

while n > total:
    total += 6 * count
    count += 1
print(count)