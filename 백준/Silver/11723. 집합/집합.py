import sys
input = sys.stdin.readline
s = set()
# def add(x):
#   s.append(x)
# def remove(x):
#   s.remove(x)
# def check(x):
#   if x in s:
#     print('1')
#   else:
#     print('0')
# def toggle(x):
#   if x in s:
#     s.remove(x)
#   else:
#     s.append(x)
# def all(x):
#   s = {i for i in range(20)}
# def empty(x):
#   s = {}
m = int(input())
for i in range(m):
  tmp = input().strip().split()
  if len(tmp) == 1:
    if tmp[0] == 'all':
      s = set([i for i in range(1, 21)])
    else:
      s = set()
    continue

  command, target = tmp[0], tmp[1]

  if command == 'add':
    s.add(int(target))
  elif command == 'check':
    print(1 if int(target) in s else 0)
  elif command == 'remove':
    s.discard(int(target))
  elif command == 'toggle':
    if int(target) in s:
      s.discard(int(target))
    else:
      s.add(int(target))