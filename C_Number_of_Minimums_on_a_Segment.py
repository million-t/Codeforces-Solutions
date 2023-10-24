
class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)
    
    def build(self, node, start, end):

        if start == end:
            self.tree[node] = (self.arr[start], 1)
            return 
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)

        if self.tree[left_child][0] == self.tree[right_child][0]:
            self.tree[node] = (self.tree[left_child][0], self.tree[left_child][1] + self.tree[right_child][1])

        elif self.tree[left_child][0] < self.tree[right_child][0]:
            self.tree[node] = self.tree[left_child]
        
        else:
            self.tree[node] = self.tree[right_child]


    def update(self, node, start, end, index, value):

        if start == end:
            self.arr[index] = value
            self.tree[node] = (value, 1)
            return 
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2

        if start <= index <= mid:
            self.update(left_child, start, mid, index, value)
        
        else:
            self.update(right_child, mid + 1, end, index, value)
        
        if self.tree[left_child][0] == self.tree[right_child][0]:
            self.tree[node] = (self.tree[left_child][0], self.tree[left_child][1] + self.tree[right_child][1])

        elif self.tree[left_child][0] < self.tree[right_child][0]:
            self.tree[node] = self.tree[left_child]
        
        else:
            self.tree[node] = self.tree[right_child]
    
    def query(self, node, start, end, left, right):

        if start > right or end < left:
            return float('inf'), 0
        
        elif left <= start and end <= right:
            return self.tree[node]
        
        mid = start + (end - start)//2
        left_child = 2*node + 1
        right_child = 2*node + 2
        left_min, left_count = self.query(left_child, start, mid, left, right)
        right_min, right_count = self.query(right_child, mid + 1, end, left, right)

        if left_min == right_min:
            return left_min, left_count + right_count
        
        elif left_min < right_min:
            return left_min, left_count
        
        return right_min, right_count




n, m = map(int, input().split())
a = list(map(int, input().split()))

tree = SegmentTree(a)
start, end = 0, n - 1

for _ in range(m):

    op_type, x, y = map(int, input().split())
    if op_type == 1:
        tree.update(0, start, end, x, y)
    
    else:
        print(*tree.query(0, start, end, x, y - 1))

