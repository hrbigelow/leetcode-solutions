class Solution {
public:
    int validSubarrays(vector<int>& nums) {
        int total = 0;
        stack<int> st;
        for (auto num : nums) {
          while (! st.empty() && st.top() > num) st.pop();
          st.push(num);
          total += st.size();
        }
        return total;
    }
};
