# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(p: TreeNode):
            if not p:
                return
            ans.append(p.val)
            dfs(p.left)
            dfs(p.right)
        dfs(root)
        return ans

# 用栈先压右再压左
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        st = [root]
        while st:
            node = st.pop()
            if node:
                ans.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return ans