class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm, counter = 0, 0
        sumMap = {0: 1}
        
        for num in nums:
            sm += num
            
            if sm - k in sumMap: counter += sumMap[sm - k]

            if sm in sumMap: sumMap[sm] += 1
            else: sumMap[sm] = 1
                
        return counter