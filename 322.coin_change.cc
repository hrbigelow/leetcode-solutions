
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
      vector<int> dp(amount+1);
      dp[0] = 0;
      for (int i=1; i<=amount; i++) {
        int min_val = INT_MAX - 1;
        for (auto c: coins) {
          if (i < c) continue;
          min_val = min(min_val, dp[i-c]);
        }
        dp[i] = min_val + 1;
      }
      return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
