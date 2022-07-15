"""
Given two nodes of a binary tree p and q, return their lowest common ancestor
(LCA).

Each node will have a reference to its parent node. The definition for Node is
below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of
two nodes p and q in a tree T is the lowest node that has both p and q as
descendants (where we allow a node to be a descendant of itself)."

"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        trail = set()
        while p is not None or q is not None:
            if p is not None:
                if p.val in trail: return p
                trail.add(p.val)
                p = p.parent
                
            if q is not None:
                if q.val in trail: return q
                trail.add(q.val)
                q = q.parent
                
        
        
"""
Solved in 11 minutes

Reasoning process started by considering special cases in which p was a direct descendant
of q or vice versa.  Also, that if p and q were at the same level, they were bound to collide.  And if
p were one level lower, they almost would collide, but then p would collide with where q was one
step before.  Then, I realized I needed to keep track of the 'trail' of q (and by symmetry p)

I also had considered whether to only store the most recent or least recent position of p or q, but
quickly realized that the lower node could intersect the upper node's trail at any position.  Therefore,
the trail had to be a set.

"""
