n = int(input())
m = map(int, raw_input().split())

my = 0
you = sum(m)
res = 0

m.sort(reverse=True)

for i in range(n):
    my += m[i]
    you -= m[i]
    if my > you:
        print(i+1)
        break


