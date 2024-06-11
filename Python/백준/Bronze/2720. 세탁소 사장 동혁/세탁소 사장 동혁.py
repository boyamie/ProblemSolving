t = int(input())
change = {'Q':25, 'D':10, 'N': 5, 'P': 1}
for i in range(t):
    c = int(input())
    q = c//change['Q']
    q_next = c%change['Q']
    d = q_next//change['D']
    d_next = q_next%change['D']
    n = d_next//change['N']
    n_next = d_next%change['N']
    p = n_next//change['P']
    print(q, d, n, p)