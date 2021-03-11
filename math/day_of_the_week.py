def isLeapYear(yr):
    if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0): return True
    return False

def leapYearsTill(yr: int):
    l = 0
    for y in range(1, yr):
        if isLeapYear(y): l += 1
    return l

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a strings
    def solve(self, A, B, C):
        weekName = {
            0: 'sunday',
            1: 'monday',
            2: 'tuesday',
            3: 'wednesday',
            4: 'thursday',
            5: 'friday',
            6: 'saturday',
        }
        monthMapping = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30
        }
        
        daysForDate = (C - 1) * 365 + leapYearsTill(C)
        curMonth = 1
        
        while curMonth < B:
            daysForDate += monthMapping[curMonth]
            curMonth += 1
            
        if isLeapYear(C) and B > 2:
            daysForDate += 1
            
        daysForDate += A
        
        return weekName[daysForDate % 7]
        
        