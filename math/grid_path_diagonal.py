import math

def solve(n):
    # The situation can fits cataln numbers' premise
    # To reach from (0, 0) to (n-1, n-1), n-1 horizontal 
    # and n-1 vertical steps need to be taken
    # For all the sequences/combinations possible from these
    # only the ones which always have vertical (the +1) > horizontal (the -1)
    # are required (for the without-crossing-diagonal part)
    # This would be equal to the (n-1)th Catalan number
    
    return (math.factorial(2 * n - 2) // (math.factorial(n) * math.factorial(n-1))) % int(1e9 + 7)