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
		))
}

func max(a, b int) int {
    if a > b {
        return a
    }
    
    return b
}

/**
 * @input A : 2D integer array 
 * 
 * @Output Integer
 */
func solve(A [][]int )  (int) {
    n, m := len(A), len(A[0])
    sumMatrix := make([][]int, n)
    
    for i := 0; i < n; i++ {
        sumMatrix[i] = make([]int, m)
    }
    
    for i := n - 1; i >= 0; i-- {
        for j := m - 1; j >= 0; j-- {
            sumMatrix[i][j] = A[i][j]
            
            if i < n - 1 {
                sumMatrix[i][j] += sumMatrix[i + 1][j]
            }
        }
    }
    
    maxSum := A[n - 1][m - 1]
    for i := n - 1; i >= 0; i-- {
        for j := m - 1; j >= 0; j-- {
            if j < m - 1 {
                sumMatrix[i][j] += sumMatrix[i][j + 1]
            }
            
            maxSum = max(maxSum, sumMatrix[i][j])
        }
    }
    
    return maxSum
}
