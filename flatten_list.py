class TreeNode:
    def __init__(self, val=0, left=None, right=None)
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None: return

        stack = []
        stack.append(root)

        while len(stack) != 0:
            current_node = stack.pop()

            if current_node.right != None:
                stack.append(current_node.right)

            if current_node.left != None:
                stack.append(current_node.left)

            if len(stack) != 0:
                current_node.right = stack[-1]

            current_node.left = None
