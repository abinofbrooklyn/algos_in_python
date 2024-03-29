class MyHashMap:
    def __init__(self):
        self.golden_ratio = 1.618
        self.table_size = 65536
        self.table = [[] for _ in range(self.table_size)]
        self.hash = lambda i: i*math.ceil(self.golden_ratio * self.table_size) % self.table_size

    def put(self, key, value):
        self.remove(key)
        hkey = self.hash(key)
        self.table[hkey].append((key, value))

    def get(self, key):
        hkey = self.hash(key)
        idx = -1
        for i, x in enumerate(self.table[hkey]):
            if x[0] == key:
                idx = i
        return -1 if idx == -1 else self.table[hkey][idx][1]

    def remove(self, key):
        hkey = self.hash(key)
        idx = -1
        for i, x in enumerate(self.table[hkey]):
            if x[0] == key:
                idx = i
        if idx >= 0:
            del self.table[hkey][idx]
