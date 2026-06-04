# Definition for a binary tree node.
#class TreeNode:
    #def __init__(self, val=0, left=None, right=None):
        #self.val = val
        #self.left = left
        #self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root is None:
            return 0
        else:
            hleft = self.maxDepth(root.left)
            hright = self.maxDepth(root.right)
            if hleft > hright:
                return hleft+1
            else:
                return hright+1

        