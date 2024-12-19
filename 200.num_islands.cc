class Solution {
  public:
    using Grid = vector<vector<char>>;
    using Virgin = vector<vector<bool>>;
    using Queue = queue<pair<size_t, size_t>>;

    int numIslands(Grid& grid) {
      if (grid.empty() || grid[0].empty()) return 0;
      int count = 0;
      size_t R = grid.size(), C = grid[0].size();
      Queue q;
      // cout << R << '\t' << C << endl;
      Virgin virgin(R, vector<bool>(C, true)); // squares that haven't ever been touched
      for (size_t i=0; i < R; i++) {
        for (size_t j=0; j < C; j++) {
          if (! virgin[i][j] || grid[i][j] == '0') continue;
          // a virgin island square
          q.emplace(i, j);
          virgin[i][j] = false;
          count++;
          while (! q.empty()) {
            auto [i2, j2] = q.front();
            q.pop();
            if (i2 + 1 < R && grid[i2+1][j2] == '1' && virgin[i2+1][j2]) {
              q.emplace(i2+1, j2);
              virgin[i2+1][j2] = false;
            }
            if (i2 > 0     && grid[i2-1][j2] == '1' && virgin[i2-1][j2]) {
              q.emplace(i2-1, j2);
              virgin[i2-1][j2] = false;
            }
            if (j2 + 1 < C && grid[i2][j2+1] == '1' && virgin[i2][j2+1]) {
              q.emplace(i2, j2+1);
              virgin[i2][j2+1] = false;
            }
            if (j2 > 0     && grid[i2][j2-1] == '1' && virgin[i2][j2-1]) {
              q.emplace(i2, j2-1);
              virgin[i2][j2-1] = false;
            }
          }
        }
      }
      return count;
    }
};

/* The important thing to realize with this problem is that there are implicitly
 * three separate states for each grid location:
 *
 * unvisited - not ever enqueued
 * pending -   enqueued
 * visited -   popped
 *
 * Since you don't want to enqueue a given position more than once, you should
 * distinguish between unvisited and (pending + visited).
 * Therefore, mark this status when you enqueue, not when you deque.
 *
 * 
 */
