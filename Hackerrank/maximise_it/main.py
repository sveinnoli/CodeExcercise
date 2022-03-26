def f(x):
    return x*x
m = [int(n) for n in input().split()[1::]]
e = [int(n) for n in input().split()[1::]]
d = [int(n) for n in input().split()[1::]]
k = [int(n) for n in input().split()[1::]]
result = []
for n in e:
    for i in d:
        for j in k:
            result.append((f(n) + f(i) + f(j))%m[0])
print(max(result))
