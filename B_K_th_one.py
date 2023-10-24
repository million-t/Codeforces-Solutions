
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
        self.tree[node] = self.tree[left_child] + self.tree[right_child]


    def update(self, node, start, end, index):

        if start == end:
            self.arr[index] = 1 - self.arr[index]
            self.tree[node] = self.arr[index]
            return 
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2

        if start <= index <= mid:
            self.update(left_child, start, mid, index)
        
        else:
            self.update(right_child, mid + 1, end, index)
        
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, node, start, end, pos):

        if start == end:
            return start
        

        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2

        left_ones = self.tree[left_child]
        right_ones = self.tree[right_child]

        if left_ones >= pos:
            return self.query(left_child, start, mid, pos)
        
        else:
            return self.query(right_child, mid + 1, end, pos - left_ones)
        





n, m = map(int, input().split())
a = list(map(int, input().split()))
ops = []

for line in range(m):
    ops.append(tuple(map(int, input().split())))

start = 0
node = 0
end = n - 1
seg_tree = SegmentTree(a)
ans = []

for op_type, param in ops:
    if op_type == 1:
        seg_tree.update(node, start, end, param)
    
    else:
        ans.append(seg_tree.query(node,start, end, param + 1))

for ind in ans:
    print(ind)