import sys

def main(lines):
    N, X = lines[0]
    S = lines[1]
    
    srt = 0
    end = N-1
    while srt<=end:
        idx = (srt+end) // 2
        if S[idx] < X:
            srt = idx + 1
        elif S[idx] > X:
            end = idx - 1
        else:
            print(idx+1)
            break
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)