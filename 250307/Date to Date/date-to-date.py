m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# if m2 == m1:
#     print(d2 - d1 + 1)
# elif abs(m2 - m1) == 1:
#     print(months[m2 - 1] - d1 + d2)
# else:
#     days = 0
#     for i in range(m1, m2 + 1):
#         if i == m1:
#             days += months[i - 1] - d1 + 1
#         elif i == m2:
#             days += d2
#         else:
#             days += months[i]
#     print(days)

if m2 == m1:
    print(d2 - d1 + 1)
elif m2 - m1 == 1:
    print(d2 + (months[m1 - 1] - d1 + 1))
else:
    days = 0
    for i in range(m1, m2 + 1):
        if m1 == i:
            days += months[i - 1] - d1 + 1
        elif m2 == i:
            days += d2
        else:
            days += months[i - 1]
    print(days)
