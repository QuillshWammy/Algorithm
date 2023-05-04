import sys

def main(lines):
    act_num = lines[0][0]
    res = lines[1]
    que_num = lines[2][0]
    que_lst = lines[3:]
    
    hit_sum = []
    miss_sum = []
    
    hit = 0
    miss = 0
    for num in range(act_num):
        if res[num] == 1:
            hit += 1
        else:
            miss += 1
        hit_sum.append(hit)
        miss_sum.append(miss)
    
    for num in range(que_num):
        que = que_lst[num]
        srt = que[0] - 1
        end = que[1] - 1
        
        if srt == 0:
            hit_num = hit_sum[end]
            miss_num = miss_sum[end]
        
        else:
            hit_num = hit_sum[end] - hit_sum[srt-1]
            miss_num = miss_sum[end] - miss_sum[srt-1]
    
        if hit_num > miss_num:
            print('win')
        elif hit_num == miss_num:
            print('draw')
        else:
            print('lose')
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)