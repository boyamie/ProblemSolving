def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string=my_string.replace(i,' ')
    lst = list(map(int,my_string.split()))
    return sum(lst)
    