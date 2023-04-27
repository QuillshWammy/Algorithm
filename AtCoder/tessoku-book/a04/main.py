import sys
import math

def main(lines):
    n_10 = lines[0][0]
    digits = int(math.log2(n_10))
    blank_num = 10 - digits
    n_2 = [0 for i in range(1, blank_num)]

    while len(n_2) < 10:
        if n_10 >= 2**digits:
            n_10 = n_10 - 2**digits
            n_2.append(1)
        else:
            n_2.append(0)            
        digits -= 1
    result = ''.join(str(j) for j in n_2)
    print(result)
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)