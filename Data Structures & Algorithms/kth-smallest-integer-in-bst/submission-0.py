# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in this problem covers kth Smallest integer in the BST
        #so i decided to solve this problem using inorder.
        arr = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return arr[k-1]




        