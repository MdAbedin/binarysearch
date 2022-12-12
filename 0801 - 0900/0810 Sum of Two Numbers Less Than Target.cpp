int solve(vector<int>& nums, int target) {
    sort(nums.begin(),nums.end());
    vector<int> new_nums;
    int ans = INT_MIN;

    for(auto num : nums){
        int l = 0, r = new_nums.size()-1;

        while(l <= r){
            int mid = (l+r)/2;

            if(new_nums[mid]+num < target){
                ans = max(ans, new_nums[mid]+num);
                l = mid+1;
            } else{
                r = mid-1;
            }
        }
        
        new_nums.push_back(num);
    }

    return ans;
}
