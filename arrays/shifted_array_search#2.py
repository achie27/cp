def binarySearch(shiftArr, l, r, num):
  while l <= r:
    mid = (l + r)//2
    if shiftArr[mid] == num:
      return mid
    elif shiftArr[mid] > num:
      r = mid - 1
    else:
      l = mid + 1
      
  return -1

def findPivot(shiftArr):
  l, r = 0, len(shiftArr) - 1
  
  while l <= r:
    mid = (l + r)//2
    if mid > 1 and shiftArr[mid] < shiftArr[mid - 1]: return mid
    
    if shiftArr[mid] >= shiftArr[l]: l = mid + 1
    
    if shiftArr[mid] <= shiftArr[r]: r = mid - 1
    
  return 0

def shifted_arr_search(shiftArr, num):
  pivot = findPivot(shiftArr)
  a = binarySearch(shiftArr, pivot, len(shiftArr) - 1, num)
  
  if a != -1: return a
  
  if (pivot > 0):
    return binarySearch(shiftArr, 0, pivot - 1, num)
  
  return -1