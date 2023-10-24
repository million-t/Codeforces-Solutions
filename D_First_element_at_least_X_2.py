


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)
    
    def build(self, node, start, end):

        if start == end:
            self.tree[node] = self.arr[start]
            return
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])


    def update(self, node, start, end, index, value):

        if start == end:
            self.arr[index] = value
            self.tree[node] = value
            return 
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2

        if start <= index <= mid:
            self.update(left_child, start, mid, index, value)
        
        else:
            self.update(right_child, mid + 1, end, index, value)
        
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])
    
    def query(self, node, start, end, x, l):

        if self.tree[node] < x or l > end:
            return -1

        elif start == end:
            return start
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2
        
        left_max = self.tree[left_child]
        right_max = self.tree[right_child]

        ans = -1
        if left_max >= x and l <= mid:
            ans = self.query(left_child, start, mid, x, l)

        if right_max >= x and ans == -1:
            ans = self.query(right_child, mid + 1, end, x, l)        
        
        return ans


n, m = map(int, input().split())
a = list(map(int, input().split()))
ops = []

for line in range(m):
    ops.append(tuple(map(int, input().split())))


start = node = 0
end = n - 1
seg_tree = SegmentTree(a)
ans = []

for op in ops:
    if op[0] == 1:
        seg_tree.update(node, start, end, op[1], op[2])
    
    else:
        ans.append(seg_tree.query(node, start, end, op[1], op[2]))

for ind in ans:
    print(ind)
