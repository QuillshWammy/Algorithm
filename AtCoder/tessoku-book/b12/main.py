import sys

def main(lines):
    N = lines[0][0]
    
    srt = 0
    end = N
    
    while srt <= end:
        mid = (srt+end)//2
        res = mid ** 3 + mid
        if res >= N:
            srt = mid+1
        else:
            end = mid-1
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)