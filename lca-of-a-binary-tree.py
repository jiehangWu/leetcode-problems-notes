# 236. Lowest common ancestor of a binary tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# Input are: root of the tree, and two other nodes

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
# recursive solution
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    elif left:
        return left
    else:
        return right

# iterative solution
def lca_iter(root, p, q):
    parent = {root: None}
    stack = [root]
    while stack and (p not in parent or q not in parent) :
            node = stack.pop(-1)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
        
    while q:
        if q in ancestors:
            return q
        q = parent[q]
        
    return root

root, n1, n2, n3, n4 = Node(3), Node(1), Node(2), Node(5), Node(6)

root.left = n1
root.right = n2
n1.left, n1. right = n3, None
n2.right = n4

print(lca_iter(root, n1, n4) == lca(root, n1, n4))
