class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
      // initialize first row of dp
      int C=grid[0].size();
      vector<int> buf1(C, INT_MAX);
      buf1[0] = 0;
      vector<int> buf2(C);
      vector<int> *pre = &buf1, *cur = &buf2;
      for (auto row: grid) {
        (*cur)[0] = (*pre)[0] + row[0];
        for (int i=1; i!=C; i++) {
          (*cur)[i] = min((*pre)[i], (*cur)[i-1]) + row[i];
        }
        std::swap(cur, pre);
      }
      return (*pre).back();
    }
};

/*

1 3 1
1 5 1
4 2 1


*/



