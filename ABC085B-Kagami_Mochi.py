N = int(input())
Mochi = [0]*N

for mochi_i in range(N):
    Mochi[mochi_i] = int(input())

print(len(set(Mochi)))