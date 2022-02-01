class DLNode:
    def __init__(self, pre=None, nxt=None, key=None, val=None):
        self.pre = pre
        self.nxt = nxt
        self.key = key
        self.val = val
        
    def insert(self, pre, nxt):
        self.pre = pre
        self.nxt = nxt
        pre.nxt = self
        nxt.pre = self
    
    def excise(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.old = DLNode()
        self.new = DLNode()
        self.old.nxt = self.new
        self.new.pre = self.old
        self.ent = dict()
        
    def _touch(self, node):
        node.excise()
        node.insert(self.new.pre, self.new)
        
        
    def get(self, key: int) -> int:
        if key not in self.ent:
            return -1
        self._touch(self.ent[key])
        return self.ent[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.ent:
            nd = self.ent[key]
            nd.val = value
            self._touch(nd)
        else:
            if len(self.ent) == self.capacity:
                del self.ent[self.old.nxt.key]
                self.old.nxt.excise()
            
            nd = DLNode(None, None, key, value)
            nd.insert(self.new.pre, self.new)
            self.ent[key] = nd
            
            
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
