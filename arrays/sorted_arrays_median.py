def medianCalc(a, b):
    m, n = len(a), len(b)
    
    firstHalf = (m + n + 1)//2
    
    low, high = 0, min(firstHalf, m)
    
    while low <= high:
        i = low + (high - low)//2
        j = firstHalf - i
        
        if i > 0 and j < n and a[i - 1] > b[j]:
            high = i - 1
        elif j > 0 and i < m and b[j - 1] > a[i]:
            low = i + 1
        else:
            median1 = 0
            if i == 0:
                median1 = b[j - 1]
            elif j == 0:
                median1 = a[i - 1]
            else:
                median1 = max(a[i - 1], b[j - 1])
    
            if (m + n)%2 == 1:
                return 1.0 * median1
            
            median2 = 0
            
            if i == m:
                median2 = b[j]
            elif j == n:
                median2 = a[i]
            else:
                median2 = min(a[i], b[j])
        
            return (median1 + median2)/2
        
    
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            return medianCalc(nums1, nums2)
        else:
            return medianCalc(nums2, nums1)