''' 情報の入力 '''
A = int(input())
B = int(input())
C = int(input())
X = int(input())

''' 結果の初期化 '''
num_pattern = 0

# 50yen, 100yen, 500yenの各個数
coins = [int(X/50), int((X/50)//2), int((X/50)//10)]
for num_coin_50 in range(coins[0]+1):
    for num_coin_100 in range(coins[1]+1):
        for num_coin_500 in range(coins[2]+1):
            if num_coin_50*50 + num_coin_100*100 + num_coin_500*500 == X:
                if num_coin_500<=A and num_coin_100<=B and num_coin_50<=C:
                    num_pattern += 1


''' 結果の出力 '''
print(num_pattern)
