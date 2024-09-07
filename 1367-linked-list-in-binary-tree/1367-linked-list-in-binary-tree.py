class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # Start DFS search from every node in the tree
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def dfs(self, head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
        if not head:  # We've matched the entire linked list
            return True
        if not node:  # Tree node is null, no path to match
            return False
        if head.val != node.val:  # Values don't match
            return False
        
        # Recursively check the left and right subtree
        return self.dfs(head.next, node.left) or self.dfs(head.next, node.right)
