from collections import defaultdict

class Solution:

    white, gray, black = 0, 1, 2

    def dfs_visit(self, edge_map, color, parent, node):
        color[node] = self.gray
        for next_node in edge_map[node]:
            if color[next_node] == self.white:
                parent[next_node] = node
                self.dfs_visit(edge_map, color, parent, next_node)
        color[node] = self.black
    
    def find_root(self, node, parent):
        while parent[node] is not None:
            node = parent[node]
        return node

    def get_nodes(self, eqs):
        nodes = set()
        for src, _, _, trg in eqs:
            nodes.add(src)
            nodes.add(trg)
        return list(nodes)
    
    def get_edgemap(self, eqs):
        edge_map = defaultdict(list)
        for src, op1, _, trg in eqs:
            if op1 == '=':
                edge_map[src].append(trg)
                edge_map[trg].append(src)
        return edge_map

    def equationsPossible(self, equations: List[str]) -> bool:
        nodes = self.get_nodes(equations)
        edge_map = self.get_edgemap(equations)
        n = len(nodes)
        color = { node: self.white for node in nodes }
        parent = { node: None for node in nodes }
        for node in nodes:
            if color[node] == self.white:
                self.dfs_visit(edge_map, color, parent, node)
        
        for src, op1, _, trg in equations:
            if op1 == '=':
                continue
            src_root = self.find_root(src, parent)
            trg_root = self.find_root(trg, parent)
            if src_root == trg_root:
                return False
        return True


