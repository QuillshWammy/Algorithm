import sys

def main(lines):
    num = str(lines[0][0])
    
    ans = 0
    for i in range(len(num)):
        ans += int(num[-(i+1)]) * 2 ** i
    print(ans)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)