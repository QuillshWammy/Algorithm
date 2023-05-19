import sys

def main(lines):
    
    N = lines[0][0]
    capa_lst = lines[1]
    D = lines[2][0]
    room_lst = lines[3:]
    
    left_max = [0] + capa_lst 
    for i in range(1, N+1):
        left_max[i] = max(left_max[i], left_max[i-1])
    
    right_max = capa_lst + [0]
    for i in range(2, N+2):
        right_max[-i] = max(right_max[-i], right_max[-(i-1)])
        
    for day in range(D):
        left, right = room_lst[day]
        print(max(left_max[left-1], right_max[right]))
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)