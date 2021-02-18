/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
 pair<int,int> helper(Tree* root){
   if(!root) return {0,0};
   pair<int,int> l = helper(root->left);
   pair<int,int> r = helper(root->right);

   if(l.first == r.first) return {l.first+1, max(l.second,r.second)+root->val};
   else if(l.first > r.first) return {l.first+1, l.second+root->val};
   else return {r.first+1, r.second+root->val};
 }

int solve(Tree* root) {
    return helper(root).second;
}
