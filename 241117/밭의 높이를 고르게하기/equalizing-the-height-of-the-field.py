N, H, T = map(int, input().split())

H_info = list(map(int, input().split()))

C = N - T + 1

min_price = None

for i in range(C):
    check_list = H_info[i:T+i].copy()

    price = 0

    for index, value in enumerate(check_list):
        price += abs(value - H)

    if min_price == None:
        min_price = price

    if min_price > price:
        min_price = price

print(min_price)