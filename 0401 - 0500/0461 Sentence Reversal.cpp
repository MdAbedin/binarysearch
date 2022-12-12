vector<string> solve(vector<string>& sentence) {
    string s;

    for(auto s2 : sentence){
      s += s2;
    }

    vector<string> ans(sentence.size());
    int i = 0;

    int last = s.size(), next = s.size();
    while ((next = s.rfind(" ", last)) != string::npos){
      for(auto c : s.substr(next+1, last-next)){
        ans[i] = c;
        ++i;
      }
      ans[i] = " ";
      ++i;
      last = next-1;
    }
    for(auto c : s.substr(0, last+1)){
      ans[i] = c;
      ++i;
    }

    return ans;
}
