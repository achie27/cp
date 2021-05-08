#
# (())
# (())
# ())(

def bracket_match(text):
  unmatched_open_brackets = 0
  unmatched_closing_brackets = 0
  
  for i, c in enumerate(text):
    if c == '(':
      unmatched_open_brackets += 1
    else:
      if unmatched_open_brackets > 0:
        unmatched_open_brackets -= 1
      else:
        unmatched_closing_brackets += 1
        
  return unmatched_open_brackets + unmatched_closing_brackets