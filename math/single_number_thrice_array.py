def singleNumber(A):
    '''
    It constructs the element appearing once by
    attempting to set the 1 bits which appeared
    either once or four times (the only possibilities here) 
    '''
    MAX_BITS = 64
    curBitPosition = 0
    ele = 0
    
    while curBitPosition <= MAX_BITS:
        bit_val = 2**curBitPosition
        total1s = 0
        
        for x in A:
            total1s += 1 if x & bit_val > 0 else 0
        
        if total1s % 3 == 1:
            ele = ele | bit_val
            
        curBitPosition += 1
            
    return ele