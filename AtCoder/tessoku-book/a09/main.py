import sys

def main(lines):
    H, W, N = lines[0]
    snow_lst = lines[1:]
    
    X = [[0]*(W+2) for _ in range(H+2)]
    
    for snow in snow_lst:
        a, b, c, d = snow
        X[a][b] += 1
        X[c+1][d+1] += 1
        X[c+1][b] -= 1
        X[a][d+1] -= 1
    
    for row in range(H):
        for axe in range(W):
            X[row+1][axe+1] += X[row][axe+1]+X[row+1][axe]-X[row][axe]
    
    for R in X[1:-1]:print(*R[1:-1])
            
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)