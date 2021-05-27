N, A, B = map(int, input().split())

result = 0

for n in range(N):
    n = n+1
    x_place = [0, 0, 0, 0, 0]

    #     1の位
    x_place[0] = (n % 10)

    #    10の位
    if 10 <= n:
        x_place[1] = (((n % 100) - (n % 10)) / 10)

    #   100の位
    if 100 <= n:
        x_place[2] = (((n % 1000) - (n % 100)) / 100)

    #  1000の位
    if 1000 <= n:
        x_place[3] = (((n % 10000) - (n % 1000)) / 1000)

    # 10000の位
    if 10000 <= n:
        x_place[4] = ((n - (n % 10000)) / 10000)

    if A <= sum(x_place) and sum(x_place) <= B:
        result += n


print(result)
