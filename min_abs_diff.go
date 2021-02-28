import "sort"
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

/**
 * @input A : Integer array
 * 
 * @Output Integer
 */
func solve(A []int )  (int) {
    sort.Ints(A)
    
    min_diff := 1000000001
    
    for i := 1; i < len(A); i++ {
        min_diff = min(min_diff, A[i] - A[i-1])
    }
    
    return min_diff
}
