import sys
import bisect

def Enumerate(A):
    sum_lst = []
    for i in range(2**len(A)):
        sum = 0
        for j in range(len(A)):
            den = (2**j)
            if (i//den) % 2 == 1:
                sum += A[j]
        sum_lst.append(sum)
    return sum_lst

def main(lines):
    N, K = lines[0]
    A = lines[1]
    
    mid = N // 2
    
    L1 = A[0:(N//2)]
    L2 = A[(N//2):N]
    
    sum_1 = Enumerate(L1)
    sum_2 = Enumerate(L2)
    sum_1.sort()
    sum_2.sort()
    
    for i in range(len(sum_1)):
        pos = bisect.bisect_left(sum_2, K-sum_1[i])
        if pos<len(sum_2) and sum_2[pos]==K-sum_1[i]:
            print("Yes")
            sys.exit(0)
    print("No")
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)