# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def dfs(node):
            if node != None:
                dfs(node.left)
                answer.append(node.val)
                dfs(node.right)
        dfs(root)
        return answer