import sys

def main(lines):
    num, tar = lines[0]
    num_list = lines[1]
    
    if tar in num_list:
        print("Yes")
    else:
        print("No")
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)