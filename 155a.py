input()
res = map(int,raw_input().split())
result = 0
max = min = res[0]

for i in res[1:]:
    if i > max: max = i; result+=1
    if i < min: min = i; result+=1

print(res)
print(result)
