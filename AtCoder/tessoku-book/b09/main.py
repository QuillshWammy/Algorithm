import sys

def main(lines):
    N = lines[0][0]
    points = lines[1:]
    s = [[0]*1501 for _ in range(1501)]
    
    for point in points:
        a, b, c, d = point
        s[a][b] += 1
        s[a][d] -= 1
        s[c][b] -= 1
        s[c][d] += 1
    
    for row in range(1501):
        for axe in range(1, 1501):
            s[row][axe] += s[row][axe-1]
    
    for axe in range(1501):
        for row in range(1, 1501):
            s[row][axe] += s[row-1][axe]
    
    cnt = 0
    for row in range(1501):
        for axe in range(1501):
            if s[row][axe] >= 1:
                cnt += 1
    print(cnt)
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)