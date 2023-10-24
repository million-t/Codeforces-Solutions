
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
        self.tree[node] = min(self.tree[left_child], self.tree[right_child])


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
        
        self.tree[node] = min(self.tree[left_child], self.tree[right_child])
    
    def query(self, node, start, end, left, right):

        if start > right or end < left:
            return float('inf')
        
        elif left <= start and end <= right:
            return self.tree[node]
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2
        left_min = self.query(left_child, start, mid, left, right)
        right_min = self.query(right_child, mid + 1, end, left, right)

        return min(left_min, right_min)




n, m = map(int, input().split())
a = list(map(int, input().split()))

tree = SegmentTree(a)
start, end = 0, n - 1

for _ in range(m):

    op_type, x, y = map(int, input().split())
    if op_type == 1:
        tree.update(0, start, end, x, y)
    
    else:
        print(tree.query(0, start, end, x, y - 1))

