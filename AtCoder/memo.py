import sys

def main(lines):
    step_num = int(lines[0])
    
    routes = [['#' for j in range(50)] for i in range(50)]
    x, y = 0, 0
    routes[x][y] = 'S'
    
    for step in range(step_num):
        y += 1
        if step+1 == step_num:
            routes[x][y] = 'G'
        else:
            routes[x][y] = '.'
    
    print()
    for row in routes:
        for col in row:
            print(col, end='')

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)