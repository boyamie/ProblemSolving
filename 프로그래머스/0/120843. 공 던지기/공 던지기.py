def solution(numbers, k):
    man = numbers[0::2] if len(numbers) % 2 == 0 else numbers[0::2] + numbers[1::2]
    answer = man[(k % len(man))-1]
    return answer