def solution(order):
    cnt = 0
    st = str(order)
    cnt += st.count(str(3))
    cnt += st.count(str(6))
    cnt += st.count(str(9))
    return cnt