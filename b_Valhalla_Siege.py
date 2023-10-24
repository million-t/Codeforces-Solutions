from bisect import bisect_right


num_warriors, num_mins = map(int, input().split())

warriors = list(map(int, input().split()))
mins = list(map(int, input().split()))


for i in range(1, num_warriors):
    warriors[i] += warriors[ i - 1]

prev_arrows = 0
start = 0
end = num_warriors

for arrows in mins:
    taken_down = bisect_right(warriors, arrows + prev_arrows, start, end)

    if taken_down == end:
        start = prev_arrows = 0
        print(num_warriors)
    
    else:
        prev_arrows += arrows
        start = taken_down
        print(num_warriors - taken_down)



        
