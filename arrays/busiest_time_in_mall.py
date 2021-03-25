def find_busiest_period(data):
  '''
  [ [1487799425, 14, 1], 
     [1487799425, 4,  0],
     [1487799425, 2,  0],
     [1487800378, 10, 1],
     [1487801478, 18, 0],
     [1487801478, 18, 1],
     [1487901013, 1,  0],
     [1487901211, 7,  1],
     [1487901211, 7,  0] ]
  '''
  
  len_data = len(data)
  i, mx_people, mx_timestamp = 0, float('-inf'), 0
  
  cumulative_count = 0
  
  while i < len_data:
    
    cur_time = data[i][0] # 1487799425
    
    abs_people = 0
    if data[i][2] == 1: abs_people += data[i][1]
    else: abs_people -= data[i][1]
  
    # abs_peope= 14
    while i + 1 < len_data and data[i + 1][0] == cur_time:
      i += 1
      
      if data[i][2] == 1: abs_people += data[i][1]
      else: abs_people -= data[i][1]
  
    if mx_people < cumulative_count + abs_people:
      mx_timestamp = cur_time
      mx_people = cumulative_count + abs_people
      
    cumulative_count += abs_people
    i += 1
  
  return mx_timestamp