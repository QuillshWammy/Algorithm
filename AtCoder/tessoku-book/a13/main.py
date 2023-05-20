import sys

def main(lines):
    N, K = lines[0]
    A = lines[1]

    R = [ None ] * N

    for i in range(0, N-1):
        if i == 0:
            R[i] = 0
        else:
            R[i] = R[i-1]
            
        while R[i] < N-1 and A[R[i]+1]-A[i] <= K:
            R[i] += 1
        
        
    ans = 0
    for i in range(0, N-1):
        ans += (R[i]-i)
    print(ans)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)