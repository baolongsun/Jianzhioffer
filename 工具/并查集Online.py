class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def reset(self):
        self.parent = {}
        self.rank = {}
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def isjoint(self,x,y):
        return self.parent[x] == self.parent[y]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank.get(root_x, 0) > self.rank.get(root_y, 0):
            self.parent[root_y] = root_x
        elif self.rank.get(root_x, 0) < self.rank.get(root_y, 0):
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] = self.rank.get(root_x, 0) + 1
if __name__ == "__main__":
    q = UnionFind()
    map_dict = {}#str:int
    # input_len = q.input()
    while True:
        w = input()
        if w == "\n":
            break
        w = w.split()
        q1,q2= w[0],w[1]
        if q1 not in map_dict:
            map_dict[q1] = len(map_dict)
        if q2 not in map_dict:
            map_dict[q2] = len(map_dict)
        q.union(map_dict[q1],map_dict[q2])

