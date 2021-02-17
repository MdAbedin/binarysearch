vector<vector<int>> solve(vector<int>& nums) {
    vector<vector<int>> ans;
    if(nums.size() == 0) return ans;
    
    sort(nums.begin(),nums.end());
    ans.push_back({nums[0],nums[0]-1});

    for(auto num : nums){
      if(num == ans.back().back()+1){
        ans.back().back() = num;
      } else{
        ans.push_back({num,num});
      }
    }

    return ans;
}
