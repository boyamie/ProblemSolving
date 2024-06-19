def solution(order):
    sum = 0
    for i in order:
        if i == "iceamericano" or i == "americanoice" or i == "hotamericano" or i == "americanohot" or i == "americano" or i == "anything":
            sum += 4500
        else:
            sum += 5000
    return sum