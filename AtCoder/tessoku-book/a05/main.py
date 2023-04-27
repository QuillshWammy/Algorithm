import sys

def main(lines):
    lim, sum_n = lines[0]
    
    cnt = 0
    for red in range(1, lim+1):
        tar = sum_n - red
        for blue in range(1, tar):
            white = tar - blue
            if blue > lim or white > lim:
                continue
            cnt += 1
    print(cnt)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)