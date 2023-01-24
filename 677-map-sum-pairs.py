class MapSum:

    def __init__(self):
        self.trie = dict()
        self.val = dict()

    def insert(self, key: str, val: int) -> None:
        if key in self.val:
            self.val[key], val = val, val - self.val[key]
        else:
            self.val[key] = val

        for i in range(1, len(key) + 1):
            if key[:i] in self.trie:
                self.trie[key[:i]] += val
            else:
                self.trie[key[:i]] = val

    def sum(self, prefix: str) -> int:
        if prefix in self.trie:
            return self.trie[prefix]
        return 0
