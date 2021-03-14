def trailingZeroes(A):
    ans, num = 0, 5
    while A // num > 0:
        ans += A//num
        num *= 5

    return ans