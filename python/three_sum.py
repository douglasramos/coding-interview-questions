# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an empty array.
# Sample Input
# array = [12, 3, 1, 2, -6, 5, -8, 6] targetSum = 0
# Sample Output
# [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# Time O(n^2) | Space O(n)
def threeNumberSum(array, targetSum):
    # Time O(n)
    numsInArray = {i:True for i in array}

    # O(nlog(n))
    array.sort()
    triplets = []

    # O(n^2)
    for idxA in range(0, len(array)):
        for idxB in range(idxA+1, len(array)):
            a = array[idxA]
            b = array[idxB]
            c = targetSum - a - b
            if b!=c!=a and c in numsInArray:
                triplet = [a,b,c]
                triplet.sort()
                triplets[tuple(triplet)] = triplet
            
    return list(triplets.values())

# Time O(n^2) | Space O(n)
# In this solution we're using the concept of left and right pointers in to tranverse the array. This is possible because the array is sorted
def threeNumberSumWithPointers(array, targetSum):
    array.sort()
    triplets = []
    # len(array)-2 because in the end of the arry we would have [..., idx, idx+1=left pointer, idx+2=right pointer]. 
    # So idx can go untill len(array)-3 and the range function is non inclusive
    for idx in range(len(array)-2):
        leftIdx = idx+1
        rightIdx = len(array)-1
        while leftIdx < rightIdx:
            currentSum = array[idx] + array[leftIdx] + array[rightIdx]
            if currentSum == targetSum:
                triplets.append([array[idx], array[leftIdx], array[rightIdx]])
                # if current sum is the target sum, then we can move both pointers, because we are certain the moving only one would make currentSum different than the target sum
                leftIdx += 1
                rightIdx -= 1
            # because the array is sorted, we know that if currentSum is yet smaller than the target sum, 
            # we can move up the left pointer to obtain a greater sum, that could potentially be the targetSum
            elif currentSum < targetSum:
                leftIdx += 1
            # because the array is sorted, we know that if currentSum is greater than the target sum, 
            # we can move dow the right pointer to obtain a smaller sum, that could potentially be the targetSum
            else:
                rightIdx -= 1
    return triplets
