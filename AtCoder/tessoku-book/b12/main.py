import sys

def f(x):
    return x ** 3 + x

def main(lines):
    N = lines[0][0]
    
    left = 0.0
    right = 100.0

    for i in range(20):
        mid = (left + right) / 2
        val = f(mid)

        if val > N:
            right = mid
        else:
            left = mid
    
    print(mid)
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)