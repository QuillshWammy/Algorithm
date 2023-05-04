import sys

def main(lines):
    num_dates, num_que = lines[0]
    vis_lst = lines[1]
    que_lst = lines[2:]
    
    sum_vis = []
    vis = 0
    for date in range(num_dates):
        vis = vis_lst[date] + vis
        sum_vis.append(vis)
        
    for num in range(num_que):
        que = que_lst[num]
        
        end = que[1] - 1

        if que[0] == 1:
            print(sum_vis[end])
        else:
            srt = que[0] - 2
            print(sum_vis[end] - sum_vis[srt])
            
        
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(list(map(int, l.split())))
    main(lines)