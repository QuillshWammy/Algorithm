import sys

def main(lines):
    A, B = lines[0]
    answer = False
    
    for num in range(A, B+1):
        if 100%num == 0:
            answer = True
            break
    
    if answer:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)