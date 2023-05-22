import sys
import bisect

def main(lines):
    N = lines[0][0]
    A = lines[1]

    X = list(set(A))
    X.sort()

    B = [None] * N
    for i in range(N):
        B[i] = bisect.bisect_left(X, A[i])
        B[i] += 1
    
    ans = [str(i) for i in B]
    print(" ".join(ans))
        
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)