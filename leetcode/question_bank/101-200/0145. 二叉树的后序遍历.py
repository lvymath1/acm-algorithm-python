# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        h = root
        st = [h]
        ans = []
        while st:
            x = st[-1]
            if x.left and h != x.left and h != x.right:
                st.append(x.left)
            elif x.right and h != x.right:
                st.append(x.right)
            else:
                ans.append(x.val)
                h = st.pop()
        return ans