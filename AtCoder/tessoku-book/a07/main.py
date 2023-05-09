import sys

def main(lines):
    D = lines[0][0]
    N = lines[1][0]
    
    attend_days = lines[2:]
    
    ans = [0] * (D+1)
        
    for i in range(N):
        attend_day = attend_days[i]
        ans[attend_day[0]-1] +=  1
        ans[attend_day[1]] += -1
        
    tmp = 0
    for i in ans[:-1]:
        tmp += i
        print(tmp)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)