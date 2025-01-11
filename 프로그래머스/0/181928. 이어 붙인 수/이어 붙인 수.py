def solution(num_list):
    even=[]
    odd=[]
    for i in num_list:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)   
    t_even = ''.join(map(str,even))  
    t_odd = ''.join(map(str,odd))
    answer = int(t_even) + int(t_odd)
    return answer
