n, k, l, c, d, p, nl, np = map(int,raw_input().split())
print(min(k*l//nl, c*d, p//np)//n)
