import sys
input = sys.stdin.readline
a = input().strip()
lth = len(a)
ha, hb = a[:lth//2], a[lth//2:]
dt = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
ra=0
rb=0
ra = sum(dt[ch] for ch in ha)
rb = sum(dt[ch] for ch in hb)

def rotate(string, rotation_value):
    rotated = ''
    for ch in string:
        rotated += chr((((ord(ch)-ord('A'))+rotation_value)%26)+ord('A'))
    return rotated
ha_rotated = rotate(ha, ra)
hb_rotated = rotate(hb, rb)
result = ''
for i in range(len(ha_rotated)):
    merged_ch = chr((((ord(ha_rotated[i])-ord('A'))+(ord(hb_rotated[i])-ord('A')))%26)+ord('A'))
    result += merged_ch
print(result)