k = int(input())
a = map(int, raw_input().split())

a.sort(reverse=True)
summ = 0

for i in range(len(a)):
    if summ < k: summ+=a[i]
    else: print(i); exit()

print(12 if summ >=k else -1)
