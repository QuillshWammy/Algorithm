N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
questions = [list(map(int, input().split())) for _ in range(Q)]

S = [[0] * (1501) for _ in range(1501)]
for point in points:
    x, y = point
    S[x][y] += 1

for i in range(1, 1501):
    for j in range(1, 1501):
        S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]

for question in questions:
    a, b, c, d = question
    ans = S[c][d] - S[c][b-1] - S[a-1][d] + S[a-1][b-1]
    print(ans)