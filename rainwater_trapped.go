package main

import ( 
	"fmt" 
)

func main() {
	fmt.Println(trap([]int{5, 1, 5}))
}

func max(a, b int) int {
    if a > b {
        return a
    }    
    return b
}

func min(a, b int) int {
    if a<b {
        return a
    }
    return b
} 

/**
 * @input A : Integer array
 * 
 * @Output Integer
 */
func trap(A []int )  (int) {
    arr_len := len(A)
    max_before := make([]int, arr_len)
    max_after := make([]int, arr_len)
    
    for i := 1; i < arr_len; i++ {
        max_before[i] = max(max_before[i - 1], A[i - 1]);
        max_after[arr_len - 1 - i] = max(max_after[arr_len - i], A[arr_len - i])
    }
    
    water := 0
    for i := 0; i < arr_len; i++ {
        if max_before[i] > A[i] && max_after[i] > A[i] {
            water += min(max_before[i], max_after[i]) - A[i]
        }
    }
    
    return water
}
