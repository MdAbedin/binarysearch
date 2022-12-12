vector<vector<int>> solve(vector<int>& nums) {
  if(nums.empty()) return {};

  vector<vector<int>> ans;

  for(auto num : nums){
    if(ans.empty() || ans.back().back() != num){
      ans.push_back({num});
    } else{
      ans.back().push_back(num);
    }
  }

  return ans;
}
