/**
 * @input A : 2D integer array 
 * 
 * @Output Integer
 */
func solve(A [][]int )  (int) {
    sum, N := 0, len(A)
    for i := 0; i < N; i++ {
        for j := 0; j < N; j++ {
            sum += (i + 1) * (j + 1) * (N - i) * (N - j) * A[i][j]
        }
    }
    
    return sum
}
