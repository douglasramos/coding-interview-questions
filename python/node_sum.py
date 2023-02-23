# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSumsRecur(node, nodeSum, sums):
    if node is None: return

    newNodeSum = nodeSum+node.value
    if not node.left and not node.right:
        sums.append(newNodeSum)
        return
        
    branchSumsRecur(node.left, newNodeSum, sums)
    branchSumsRecur(node.right, newNodeSum, sums)
    
# time O(n) | space O(n) - where n is the number of nodes in the Binary Tree    
def branchSums(root):
    sums = []
    branchSumsRecur(root, 0, sums)
    return sums


tree1 = BinaryTree(value=1)
tree2 = BinaryTree(value=2)
tree3 = BinaryTree(value=3)
tree1.left=tree2
tree1.right=tree3

print(branchSums(tree1))


def branchSumsAlternative(root):
    if root is None: return []
    branches = branchSumsAlternative(root.left) + branchSumsAlternative(root.right)

    return [x+root.value for x in branches] if branches else [root.value]