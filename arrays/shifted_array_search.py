def recur(shiftArr, l, r, num):
  if r < l: return -1
  
  if shiftArr[l] <= shiftArr[r]:
    if num < shiftArr[l] or num > shiftArr[r]: return -1
    
    mid = (l + r)//2
    if num > shiftArr[mid]:
      return recur(shiftArr, mid + 1, r, num)
    elif num < shiftArr[mid]:
      return recur(shiftArr, l, mid - 1, num)
    else:
      return mid
  else:
    mid = (l + r)//2
    a, b = recur(shiftArr, l, mid, num), recur(shiftArr, mid + 1, r, num)
    
    if a != -1: return a
    if b != -1: return b
    
    return -1
    
def shifted_arr_search(shiftArr, num):
  l, r = 0, len(shiftArr) - 1
  return recur(shiftArr, l, r, num)