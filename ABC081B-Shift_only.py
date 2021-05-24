num_input = int(input())

input_n = list(map(int, input().split()))

# 処理回数
num_exe = 0

# 終了フラグ
flag_End = False

while(flag_End == False):
    # すべて偶数であるかどうかを確認するフラグの初期化
    flag_Odd = False

    for n in range(num_input):
        # 奇数の場合
        if input_n[n] % 2 == 1:
            flag_Odd = True

    # もし全て偶数だった場合
    if flag_Odd == False:
        for n in range(num_input):
            input_n[n]=int(input_n[n]/2)
        num_exe += 1
    # もし奇数が含まれていた場合
    else:
        flag_End = True

print(num_exe)
