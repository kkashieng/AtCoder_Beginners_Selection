a, b = map(int, input().split())

# 偶数の場合
if a*b % 2 == 0:
    print("Even")
# 奇数の場合
else:
    print("Odd")