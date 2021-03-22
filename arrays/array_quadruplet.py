def find_array_quadruplet(arr, s):
  '''
  n3
  
  start
  [2, 7, 4, 0, 9, 5, 1, 3]
  
  
  [4, 4, 4, 4], 16
  '''
  
  len_arr = len(arr)
  
  if len_arr < 4:
    return []
  
  arr.sort()
  
  for i1 in range(0, len_arr):
    for i2 in range(i1 + 1, len_arr):
      
      partial_sum = s - (arr[i1] + arr[i2])
      start, end = i2 + 1, len_arr - 1
      
      while start < end:
        cur_sum = arr[start] + arr[end]
        if cur_sum == partial_sum:
          return [arr[i1], arr[i2], arr[start], arr[end]]
        elif cur_sum > partial_sum:
          end -= 1
        else:
          start += 1
        
  return []