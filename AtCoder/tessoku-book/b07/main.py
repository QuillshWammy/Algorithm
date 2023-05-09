import sys

def main(lines):
    T = lines[0][0]
    N = lines[1][0]
    
    result = [0] * (T+1)
    for worker in lines[2:]:
        result[worker[0]] += 1
        result[worker[1]] -= 1
    
    cnt = 0
    for i in result[:-1]:
        cnt += i
        print(cnt)
    
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)