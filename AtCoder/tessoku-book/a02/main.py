import sys

def main(lines):
    # 処理
    print(lines)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)