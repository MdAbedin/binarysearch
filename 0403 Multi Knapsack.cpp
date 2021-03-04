int solve(vector<int>& weights, vector<int>& values, int capacity, int count) {
    int dp[capacity+1][count+1];
    fill(&dp[0][0], &dp[0][0]+(capacity+1)*(count+1),0);

    for(int i = 0; i < weights.size(); ++i){
      int dp2[capacity+1][count+1];
      fill(&dp2[0][0], &dp2[0][0]+(capacity+1)*(count+1),0);
      copy(&dp[0][0], &dp[0][0]+(capacity+1)*(count+1), &dp2[0][0]);

      for(int w = 0; w < capacity+1; ++w){
        for(int c = 0; c < count+1; ++c){
          dp2[w][c] = max(dp2[w][c], w-weights[i]>=0 && c-1>=0 ? dp[w-weights[i]][c-1] + values[i] : 0);
        }
      }

      copy(&dp2[0][0], &dp2[0][0]+(capacity+1)*(count+1), &dp[0][0]);
    }

    return dp[capacity][count];
}
