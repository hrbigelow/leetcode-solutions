class Solution {
public:
    enum Status {
      TODO = 0,
      PEND = 1,
      DONE = 2
    };
    using Graph = vector<vector<int>>;
    int _max_depth(int node, vector<Status> &status, vector<int> &depths, Graph &graph) {
      assert(node >= 0 && node < status.size());
      if (status[node] == PEND) return INT_MAX;
      if (status[node] == DONE) return depths[node];
      status[node] = PEND;
      int depth = 0;
      for (auto nbor: graph[node]) {
        auto this_depth = _max_depth(nbor, status, depths, graph);
        depth = max(this_depth, depth);
      }
      status[node] = DONE;
      depths[node] = (depth == INT_MAX) ? INT_MAX : depth + 1;
      return depths[node];
    }

    int minimumSemesters(int n, vector<vector<int>>& relations) {
      int max_depth = 0;
      vector<Status> status(n, TODO);
      vector<int> depths(n, 0);
      Graph graph(n, vector<int>());
      for (auto &rel : relations) {
        graph[rel[0]-1].push_back(rel[1]-1);
      }
      for (int node = 0; node != n; node++) {
        int depth = _max_depth(node, status, depths, graph);
        max_depth = max(max_depth, depth);
        if (max_depth == INT_MAX) return -1;
      }
      return max_depth;
    }
};

/*
want to do a topo sort.  this is traditionally done by maintaining a global
dictionary of states: todo, pending, done  for each node in the graph.
we traverse using DFS, transitioning any node from todo->pending upon visiting,
then when returning from the node, from pending->done.

Each node experiences the two transitions exactly once.

Since the leaves don't depend on anything, they are added to the schedule first.

We want to return minimum depth, or -1 if cycle is detected.


*/
