import math

def bs(arr, l, r, char):
    if l > r: return -1
    
    mid = (l + r)//2
    
    if arr[mid] == char:
        return mid
    elif arr[mid] > char:
        return bs(arr, l, mid - 1, char)
    else:
        return bs(arr, mid + 1, r, char)

def findRank(A):
    rank = 1
    sorted_a = sorted(A)
    
    for i, c in enumerate(A):
        pos = bs(sorted_a, 0, len(sorted_a) - 1, c)
        pos *= math.factorial(len(A) - i - 1)
        rank += pos
        sorted_a.remove(c)
    
    return rank % 1000003

print(findRank("acb"))