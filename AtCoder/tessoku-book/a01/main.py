import sys

def main(lines):
    
    num = int(lines[0])
    print(num**2)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)