/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */

/**
 * class LLNode {
 *     public:
 *         int val;
 *         LLNode *next;
 * };
 */
Tree* solve(LLNode* node) {
    if(!node) return nullptr;
    auto child = solve(node->next);
    auto cur = new Tree();
    cur->val = node->val;
    if(!child || child->val < node->val) cur->left = child;
    else cur->right = child;

    return cur;
}
