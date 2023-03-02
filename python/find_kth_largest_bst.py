class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def findKthLargestValueInBstRecur(tree: BST, largestNumbers: list, k: int):
    if len(largestNumbers) >= k: return

    if tree.right is not None:
        findKthLargestValueInBstRecur(tree.right, largestNumbers, k)
    
    largestNumbers.append(tree.value)

    if tree.left is not None:
        findKthLargestValueInBstRecur(tree.left, largestNumbers, k)

        
#  Time O(h+k)| Space  O(h+k), h=log(n)
#  With this algorithm, we are sure the no matter the size of k, we will traverse at least the whole far right branch fo the tree (to find the largest number)
#  which means that we acess one node in each level of the tree, meaning that space for this operation is O(h)
#  however if k > h, it means that we need to acess extra node to get the kth largest number, so time complexity is O(k). Combine those two,
#  we conclude that if k > h -> O(k) and k < h -> O(h). In big O notation, this could be translated into O(h+k)
#  since we're using an array to keep all visited nodes, then the space complexity is also O(h+k)
def findKthLargestValueInBst(tree: BST, k: int) -> int:
    # Write your code here.
    largestNumbers = []
    findKthLargestValueInBstRecur(tree, largestNumbers, k)

    return largestNumbers[k-1]


def findKthLargestValueInBstAlternativeRecur(tree: BST, treeInfo: dict, k: int):
    if tree is None or treeInfo["numberOfVisistedNodes"] >= k: return

    findKthLargestValueInBstAlternativeRecur(tree.right, treeInfo, k)
    if treeInfo["numberOfVisistedNodes"] < k:
        treeInfo["lastVisitedNode"] = tree
        treeInfo["numberOfVisistedNodes"] += 1
    findKthLargestValueInBstAlternativeRecur(tree.left, treeInfo, k)
        

def findKthLargestValueinBstAlternative(tree:BST, k:int) -> int:
    treeInfo = {"numberOfVisistedNodes": 0, "lastVisitedNode": None}
    findKthLargestValueInBstAlternativeRecur(tree, treeInfo, k)
    return treeInfo["lastVisitedNode"].value
