N = int(input())

cards = list(map(int, input().split()))

Alice_score = 0
Bob_score = 0

for i in range(N):
    # Aliceのターン
    if i % 2 == 0:
        Alice_score += max(cards)
        cards.remove(max(cards))
    # Bobのターン
    else:
        Bob_score += max(cards)
        cards.remove(max(cards))

print(Alice_score - Bob_score)