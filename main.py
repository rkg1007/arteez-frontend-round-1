class SegmentTreeNode:
    def __init__(self, val, leftBoundary, rightBoundary, leftChild = None, rightChild = None):
        self.val = val
        self.leftBoundary = leftBoundary 
        self.rightBoundary = rightBoundary
        self.leftChild = leftChild
        self.rightChild = rightChild
        
class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.root = self.buildSegmentTree(arr, 0, n-1)
        
    def buildSegmentTree(self, arr, leftBoundary, rightBoundary):
        if leftBoundary == rightBoundary:
            return SegmentTreeNode(arr[leftBoundary], leftBoundary, rightBoundary)
        
        midBoundary = leftBoundary + (rightBoundary - leftBoundary) // 2
        leftChild = self.buildSegmentTree(arr, leftBoundary, midBoundary)
        rightChild = self.buildSegmentTree(arr, midBoundary+1, rightBoundary)
        
        currMinVal = min(leftChild.val, rightChild.val)
        currNode = SegmentTreeNode(currMinVal, leftBoundary, rightBoundary, leftChild, rightChild)
        
        return currNode
    
    def findMin(self, leftBoundary, rightBoundary):
        return self.findMinHelper(self.root, leftBoundary, rightBoundary)
        
    def findMinHelper(self, node, leftBoundary, rightBoundary):
        if (rightBoundary < node.leftBoundary or node.rightBoundary < leftBoundary):
            # no overlap
            return float('inf')
        
        if (leftBoundary <= node.leftBoundary and node.rightBoundary <= rightBoundary):
            # full overlap
            return node.val
        
        return min(
            self.findMinHelper(node.leftChild, leftBoundary, rightBoundary),
            self.findMinHelper(node.rightChild, leftBoundary, rightBoundary)
        )
    
    
class Solution:
    def isPossibleAns(self, arr, segmentTree, target):
        n = len(arr)
        for i in range(n):
            if arr[i] >= target and i + target - 1 < n:
                if segmentTree.findMin(i, i + target - 1) >= target:
                    return True
        return False
    
    def solution(self, arr):
        segmentTree = SegmentTree(arr)
        n = len(arr)
        ans = 0
        low, high = 0, n
        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossibleAns(arr, segmentTree, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    solution = Solution()
    print(solution.solution(arr))
