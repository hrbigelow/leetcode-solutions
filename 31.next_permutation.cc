class Solution {
  public:
    void nextPermutation(vector<int>& nums) {
      int j = nums.size() - 1, n = nums.size();
      int prev_val = INT_MIN;
      while (j != 0 && nums[j-1] >= nums[j]) j--;
      if (j == 0) {
        std::sort(nums.begin(), nums.end());
        return;
      } 
      // [j, n) is smallest range containing a strict increase
      size_t k = n - 1;
      while (nums[k] <= nums[j-1]) k--;

      std::swap(nums[j-1], nums[k]);
      std::sort(nums.begin() + j, nums.end());
    }
};

/*


*/
