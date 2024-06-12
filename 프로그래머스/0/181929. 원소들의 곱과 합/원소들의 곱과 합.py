def solution(num_list):
    mul =1 
    for i in num_list:
        mul *= i
    hap = sum(num_list)
    if mul < hap**2:
        return 1
    elif mul > hap**2:
        return 0