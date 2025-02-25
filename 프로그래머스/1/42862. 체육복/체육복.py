def solution(n, lost, reserve):
    reserved = set(reserve) - set(lost)
    losted = set(lost) - set(reserve)
    
    for r in reserved:
        if r-1 in losted:
            losted.remove(r-1)
        elif r+1 in losted:
            losted.remove(r+1)
            
    return n - len(losted)