table = [input() for i in range(5)]

for col in range(15):
    for row in range(5):
        if col < len(table[row]):
            print(table[row][col], end = '')