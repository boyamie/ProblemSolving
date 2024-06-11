n, b = map(int, input().split())
import string

tmp = string.digits+string.ascii_lowercase
def convert(n, b):
    x, y = divmod(n, b)
    if x == 0 :
        return tmp[y]
    else:
        return convert(x,b)+tmp[y]
    
print((convert(n, b)).upper())    