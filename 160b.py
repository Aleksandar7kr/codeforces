n = int(input())
t = map(int,list(str(raw_input())))

l = t[:n]; r = t[n:]
l.sort(); r.sort()

f1,f2 = 0,0

for i in range(n):
    if l[i] >= r[i]:
        f1 = 1; break
        
for i in range(n):
    if l[i] <= r[i]:
        f2 = 1; break

print("YES" if f1+f2 < 2 else "NO")

