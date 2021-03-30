class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        '''
        5 , 10 days
        10, 8 days
        20, 3 days
        40, <= 3 days
        50, 2
        60, 1
        '''
        
        low, high = max(weights) - 1, sum(weights)
        
        while high - low > 1:
            mid = low + (high - low)//2 # 30/2 -> 15  
            
            days = self.cargoLoadingTime(weights, mid) 
            
            if days > D:
                low = mid
            else:
                high = mid
                
        return high
    
    def cargoLoadingTime(self, weights, shipWeightCapacity):
        
        i, days = 0, 1
        curSum = 0

        while i < len(weights):
            curSum += weights[i]
            
            if curSum > shipWeightCapacity: #15
                days += 1
                curSum = weights[i]

            i += 1

        return days
                
        