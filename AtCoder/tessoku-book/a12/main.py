import sys

def main(lines):
    N, K = lines[0]
    A_lst = lines[1]
    A_lst.sort()
    
    srt = 0
    end = K
    
    ans = 0
    for i in range(N):
        ans += end // A_lst[i]
    print(ans)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)