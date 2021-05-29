import itertools, operator

''' 入力 '''
N, Y = list(map(int, input().split()))


for cuts in itertools.combinations_with_replacement(range(N+1), 2):
    money = list(map(operator.sub, cuts + (N,), (0,) + cuts))
    if money[0]*10000 + money[1]*5000 + money[2]*1000 == Y:
        print(money[0], money[1], money[2])
        exit()

print(-1, -1, -1)
