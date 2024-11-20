a, b = map(int, input().split())

a_temp = a

list_ = []

while(a > 1):
    list_.append(a % b)
    a = a // b

result = []
for i in range(a_temp):
    cnt = 0
    for j in list_:
        if j == i:
            cnt += 1
    result.append(cnt**2)

sum_ = 0
for i in result:
    sum_ += i

print(sum_)
