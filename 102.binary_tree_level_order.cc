/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
      vector<vector<int>> result;
      if (!root) return result;
      queue<pair<int, TreeNode*>> q;
      q.emplace(0, root);
      while (!q.empty()) {
        auto [depth, node] = q.front();
        q.pop();
        if (depth == result.size()) result.push_back(vector<int>());
        result[depth].push_back(node->val);
        if (node->left) q.emplace(depth+1, node->left);
        if (node->right) q.emplace(depth+1, node->right);
      }
      return result;
    }
};

