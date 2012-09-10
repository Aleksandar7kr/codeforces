n = int(input())
a = zip(map(int, raw_input().split()),range(1,n+1))



print a, sorted(zip(a))
