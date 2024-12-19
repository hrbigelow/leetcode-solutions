class DLNode {
  // Doubly-linked list node
  public:
  int key, val;
  DLNode *pre, *nxt; // non-ownership relation

  DLNode(int key, int val, DLNode *pre=nullptr, DLNode *nxt=nullptr) 
    : key(key), val(val), pre(pre), nxt(nxt) { }

  void excise() {
    // excise oneself from the list
    pre->nxt = nxt;
    nxt->pre = pre;
    pre = nullptr;
    nxt = nullptr;
  }

  void insert_after(DLNode *left) {
    DLNode *right = left->nxt;
    left->nxt = this;
    assert(right);
    right->pre = this;
    pre = left;
    nxt = right;
  }

};

class LRUCache {
  public:
  shared_ptr<DLNode> head, tail;
  int capacity;
  map<int, shared_ptr<DLNode>> nodes;

public:
    LRUCache(int capacity) : capacity(capacity) {
      head = make_shared<DLNode>(-1, -1);
      tail = make_shared<DLNode>(-1, -1);
      head->nxt = tail.get();
      tail->pre = head.get();
    }

    
    int get(int key) {
      if (!nodes.contains(key)) return -1;
      auto node = nodes[key];
      node->excise();
      node->insert_after(head.get());
      return node->val;
    }
    
    void put(int key, int value) {
      if (!nodes.contains(key)) {
        // cout << "did not find " << key << endl;
        if (nodes.size() == capacity) {
          auto lru = tail->pre;
          lru->excise();
          // cout << "full, deleting " << lru->key << endl;
          nodes.erase(lru->key);
        }
        auto node = std::make_shared<DLNode>(key, value);
        node->insert_after(head.get());
        nodes[key] = node;
      } else {
        auto node = nodes[key];
        node->excise();
        node->insert_after(head.get());
        node->val = value;
      }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

 /*
I assume both get and put bump the key to most recently used position.

So, you need to keep an ordering (doubly linked list?)


 */
