package main

import ( 
	"fmt" 
)

func main() {
	fmt.Println(
		solve(
			[][]int{
				[]int{ 1, 2, 3 },
				[]int{ 4, 5, 6 },
				[]int{ 7, 8, 9 },
			},
			[]int{ 1, 2 },
			[]int{ 1, 2 },
			[]int{ 2, 3 },
			[]int{ 2, 3 },
		))
}

/**
 * @input A : 2D integer array 
 * @input B : Integer array
 * @input C : Integer array
 * @input D : Integer array
 * @input E : Integer array
 * 
 * @Output Integer array.
 */
func solve(A [][]int , B []int , C []int , D []int , E []int )  ([]int) {
    N, M, Q := len(A), len(A[0]), len(B)
    prefixedSum := make([][]int, N)

	mod := 1000000007
    for i := 0; i < N; i++ {
        prefixedSum[i] = make([]int, M)
    }

    for i := 0; i < N; i++ {
        for j := 0; j < M; j++ {
            prefixedSum[i][j] = A[i][j]
            if i != 0 {
                prefixedSum[i][j] += prefixedSum[i - 1][j]
            }
        }
    }

	for i := 0; i < N; i++ {
        for j := 0; j < M; j++ {
            if j != 0 {
                prefixedSum[i][j] += prefixedSum[i][j - 1]
            }
        }
    }
    
    res := make([]int, Q)
    for i := 0; i < Q; i++ {
        b, c, d, e := B[i] - 1, C[i] - 1, D[i] - 1, E[i] - 1
        
        val := prefixedSum[d][e] 
        
        if b > 0 {
            val -= prefixedSum[b - 1][e] 
        }
        
        if c > 0 {
           val -= prefixedSum[d][c - 1]
        }
        
        // for overlapped area
        if b > 0 && c > 0 {
            val += prefixedSum[b - 1][c - 1]
        }

		for ; val < 0; {
			val += mod
		}
        
        res[i] = val % mod
    }
    
    return res
}

// [
// 	[1 3 6]
// 	[5 13 25] 
// 	[12 33 67]
// ]