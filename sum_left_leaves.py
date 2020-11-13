# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root, left)
            if not root: return
            if left and not root.left and not root.right:
                res[0] += root.val
            dfs(root.left, True)
            dfs(root.right, False)

        res = [0]
        dfs(root, False)
        return res[0]
