import sys

def sum(l, r, S):
    return S[r+1] - S[l]

def main(lines):
    N, K = lines[0]
    A = lines[1]
    
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i-1]
    R = [ None ] * N
    
    for i in range(N):
        if i == 0:
            R[i] = -1
        else:
            R[i] = R[i - 1]
        while R[i] < N-1 and sum(i,R[i]+1,S) <= K:
            R[i] += 1
    
    ans = 0
    for i in range(N):
        ans += (R[i] - i + 1)
    print(ans)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)