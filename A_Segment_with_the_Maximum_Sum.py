
import sys


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.before_change = self.build(0, 0, len(arr) - 1)
    
    def build(self, node, start, end):

        if start == end:
            val = self.arr[start]
            self.tree[node] = max(val, 0), val, val, val 
            return max(val, 0)
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2

        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)

        seg1, pref1, suf1, sum1 = self.tree[left_child] 
        seg2, pref2, suf2, sum2 = self.tree[right_child] 
        cur_seg = max(seg1, seg2, suf1 + pref2)
        cur_pref = max(pref1, sum1 + pref2)
        cur_suf = max(suf2, suf1 + sum2)
        cur_sum = sum1 + sum2

        self.tree[node] = cur_seg, cur_pref, cur_suf, cur_sum
        return cur_seg


    def update(self, node, start, end, index, value):

        if start == end:
            self.arr[index] = value
            self.tree[node] = max(value, 0), value, value, value
            return max(value, 0)
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2

        if start <= index <= mid:
            self.update(left_child, start, mid, index, value)
        
        else:
            self.update(right_child, mid + 1, end, index, value)
        
        seg1, pref1, suf1, sum1 = self.tree[left_child] 
        seg2, pref2, suf2, sum2 = self.tree[right_child] 
        cur_seg = max(seg1, seg2, suf1 + pref2)
        cur_pref = max(pref1, sum1 + pref2)
        cur_suf = max(suf2, suf1 + sum2)
        cur_sum = sum1 + sum2

        self.tree[node] = cur_seg, cur_pref, cur_suf, cur_sum
        return cur_seg
    

inp = list(sys.stdin)

n, m = map(int, inp[0].split())
a = list(map(int, inp[1].split()))
ops = []

for line in range(2, m + 2):
    ops.append(map(int, inp[line].split()))

seg_tree = SegmentTree(a)
start = 0
end = n - 1
node = 0
ans = [seg_tree.before_change]

for ind, val in ops:
    ans.append(seg_tree.update(node, start, end, ind, val))

for cur_max in ans:
    print(cur_max)

