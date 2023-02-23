# Time O(log(n)) | Space O(1)
def binarySearch(array, target):
    startIdx = 0
    endIdx = len(array)-1
    while startIdx <= endIdx:
        currentNodeIdx = (endIdx + startIdx) // 2
        currentNodeValue = array[currentNodeIdx]
        if target == currentNodeValue:
            return currentNodeIdx
        if target > currentNodeValue:
            startIdx = currentNodeIdx + 1
        if target < currentNodeValue:
            endIdx = currentNodeIdx - 1
            
    return -1


print(binarySearch([1, 5, 23, 111], 111))