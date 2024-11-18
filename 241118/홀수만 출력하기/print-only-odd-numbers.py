N = int(input())
N_list = []

for i in range(N):
    N_list.append(int(input()))

for v in N_list:
    if v % 2 != 0 and v % 3 == 0:
        print(v)
