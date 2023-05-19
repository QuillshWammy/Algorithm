import sys

def check(x, N, K, A):
    sum = 0
    for i in range(N):
        sum += x // A[i]
    if sum >= K:
        return True
    return False

def main(lines):
    N, K = lines[0]
    A = lines[1]

    left = 1
    right = 10 ** 9

    while left < right:
        mid = (left + right) // 2
        answer = check(mid, N, K, A)

        if answer == False:
            left = mid + 1
        if answer == True:
            right = mid

    print(left)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)