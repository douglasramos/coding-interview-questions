import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        min_value = self.heap[0]
        last_value = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self.sift_down(0)
        return min_value

    def sift_down(self, i):
        while i < self.size():
            min_index = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < self.size() and self.heap[left] < self.heap[min_index]:
                min_index = left
            if right < self.size() and self.heap[right] < self.heap[min_index]:
                min_index = right
            if i != min_index:
                self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
                i = min_index
            else:
                break

    def build_heap(self, arr):
        self.heap = arr[:]
        n = self.size()
        start = self.parent(n - 1)
        for i in range(start, -1, -1):
            self.sift_down(i)


# Time log(n-k) | Space O(1)
def findKthLargest(nums, k):
    heap = MinHeap()
    heap.build_heap(nums) # Time O(n) | Space O(n)
    size = len(nums)
    count_elements_to_remove = size - k
    for _ in range(count_elements_to_remove): # Time log(n-k) | Space O(1)
        heap.extract_min()
    return heap.heap[0]


def findKthLargestHeapqImpl(nums, k):
    heap = nums[:]
    heapq.heapify(heap)
    size = len(nums)
    count_elements_to_remove = size - k
    for _ in range(count_elements_to_remove): # Time log(n-k) | Space O(1)
        heapq.heappop(heap)
    return heap[0]


