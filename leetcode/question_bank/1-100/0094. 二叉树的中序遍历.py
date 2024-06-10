# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def f(p: TreeNode) -> None:
            if not p:
                return
            f(p.left)
            ans.append(p.val)
            f(p.right)
        f(root)
        return ans


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        st = []
        p = root
        while p or st:
            if p:
                st.append(p)
                p = p.left
            else:
                x = st.pop()
                ans.append(x.val)
                if x.right:
                    p = x.right
        return ans

