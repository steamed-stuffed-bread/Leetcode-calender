/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> l1;
        vector<int> l2;
        
        helper(root1, l1);
        helper(root2, l2);
        
        vector<int> res;
        res.insert(res.end(), l1.begin(), l1.end());
        res.insert(res.end(), l2.begin(), l2.end());
        
        sort(res.begin(), res.end());
        return res;
    }
    
    void helper(TreeNode* root, vector<int>& seq) {
        if (!root) return;
        
        helper(root->left, seq);
        seq.push_back(root->val);
        helper(root->right, seq);
    }
};
