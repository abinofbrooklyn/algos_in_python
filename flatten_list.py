class TreeNode:
    def __init__(self, val=0, left=None, right=None)
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is not None:
            self.flatten(root.left)
            self.flatten(root.right)

            if root.left is not None:
                current = root.left
                while current.right is not None:
                    current = current.right
                current.right = root.right
                root.right = root.left
                root.left = None
