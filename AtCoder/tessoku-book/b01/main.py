import sys

def main(lines):
    A, B = lines[0]
    print(A + B)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)