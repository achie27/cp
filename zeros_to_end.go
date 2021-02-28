package main

import ( 
	"fmt" 
)

func main() {
	fmt.Println(solve([]int{1, 2, 0, 4, 0}))
}

/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
 func solve(A []int )  ([]int) {
    for i := 0; i < len(A); i++ {
        for j := i + 1; j < len(A) && A[i] == 0; j++ {
            A[i], A[j] = A[j], A[i]
        }
    }
    
    return A
}
