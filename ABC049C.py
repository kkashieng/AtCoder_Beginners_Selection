S = input()

STR_LIST = (
    "eraser",
    "erase",
    "dreamer",
    "dream"
)

while(S):
    flag_strip = False
    for str_i in STR_LIST:
        if S.endswith(str_i):
            S = S[:-1*len(str_i)]
            flag_strip = True

    if not flag_strip:
        print("NO")
        exit()

print("YES")
