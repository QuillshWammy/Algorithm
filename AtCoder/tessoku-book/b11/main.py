import sys
import bisect

def main(lines):
    N = lines[0][0]
    A = lines[1]
    Q = lines[3:]
    
    A = sorted(A)
    
    for q in Q:
        q = q[0]
        idx = bisect.bisect_left(A, q)
        print(idx)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)