n = int(input())
t = map(int, raw_input().strip())
print('YES' if set(t+[4,7]) == set([4,7]) and sum(t[:n/2]) == sum(t[n/2:]) else 'NO')
