import sys

def main(lines):
    num = lines[0][0]
    price_lst = lines[1]
    
    ans = False
    for i in range(num):
         for k in range(i+1, num):
             for j in range(k+1, num):
                 if price_lst[i] + price_lst[k] + price_lst[j] == 1000:
                     ans = True
    
    if ans:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)