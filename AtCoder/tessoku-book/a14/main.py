import sys
import bisect

def main(lines):
    N, K = lines[0]
    A = lines[1]
    B = lines[2]
    C = lines[3]
    D = lines[4]
    
    P = []
    for x in range(N):
        for y in range(N):
            P.append(A[x]+B[y])
    
    Q = []
    for z in range(N):
        for w in range(N):
            Q.append(C[z] + D[w])
    
    Q.sort()
    
    for i in range(len(P)):
        pos1 = bisect.bisect_left(Q, K-P[i])
        if pos1 < N**2 and Q[pos1] == K-P[i]:
            print("Yes")
            sys.exit(0)
    
    print("No")
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)