stu_list = []
for i in range(28):
    stu_list.append(int(input()))
for i in range(1,31):
    if i not in stu_list:
        print(i)