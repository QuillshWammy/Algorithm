import sys

def check(mid, A, K):
    if A[mid-1] + A[mid] >= K:
        return True
    return False

def main(lines):
    N, K = lines[0]
    A = lines[1]

    left = 1
    right = N

    while left < right:
        mid = (left + right) // 2
        ans = check(mid, A, K)

        if ans:
            left = mid + 1
        else:
            right = mid - 1
    
    print(left)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)