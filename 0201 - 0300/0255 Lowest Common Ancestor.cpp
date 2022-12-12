/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */

unordered_map<Tree*,bool> has_a;
unordered_map<Tree*,bool> has_b;

 bool has_x(Tree* root, int x, bool is_a){
   if(!root) return false;
   if(is_a && has_a.find(root) != has_a.end()) return has_a[root];
   if(!is_a && has_b.find(root) != has_b.end()) return has_b[root];

   bool ans = root->val == x || has_x(root->left,x,is_a) || has_x(root->right,x,is_a);
   if(is_a) has_a[root] = ans;
   else has_b[root] = ans;

   return ans;
 }

pair<int,bool> helper(Tree* root, int a, int b){
  if(!root) return {-1, false};

  auto ans_l = helper(root->left,a,b), ans_r = helper(root->right,a,b);
  if(ans_l.second) return ans_l;
  if(ans_r.second) return ans_r;

  if(has_x(root,a,true) && has_x(root,b,false)) return {root->val, true};
  else return {-1,false};
}

int solve(Tree* root, int a, int b) {
 return helper(root, a, b).first;
}
