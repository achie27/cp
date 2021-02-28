package main

import ( 
	"fmt" 
)

func main() {
	fmt.Println(maxArr([]int{3, 1, 2}))
}

func max( a, b int ) int {
    if a > b {
        return a
    }
    
    return b
}

/**
 * @input A : Integer array
 * 
 * @Output Integer
 */
func maxArr(A []int )  (int) {
    max_of_diff_A, min_of_diff_A := A[0], A[0]
    max_of_sum_A, min_of_sum_A := A[0], A[0]
    
    arr_len := len(A)
    for i := 0; i < arr_len; i++ {
        cur_diff_A := A[i] - i
        cur_sum_A := A[i] + i
        
        if cur_diff_A < min_of_diff_A {
            min_of_diff_A = cur_diff_A
        }
        
        if cur_sum_A < min_of_sum_A {
            min_of_sum_A = cur_sum_A
        }
        
        
        if cur_diff_A > max_of_diff_A {
            max_of_diff_A = cur_diff_A
        }
        
        if cur_sum_A > max_of_sum_A {
            max_of_sum_A = cur_sum_A
        }
    }
    
    return max(max_of_sum_A - min_of_sum_A, max_of_diff_A - min_of_diff_A)
}

/*
 * - (A[i] - A[j]) + (i - j) ->   - (A[i] - i) + (A[j] - j)  -> max of diff_A[] - min of diff_A[]
 * - (A[i] - A[j]) - (i - j) ->   - (A[i] + i) + (A[j] + j)  -> max of sum_A[] - min of sum_A[]
 * + (A[i] - A[j]) + (i - j) ->   + (A[i] + i) - (A[j] + j)
 * + (A[i] - A[j]) - (i - j) ->   + (A[i] - i) - (A[j] - j)
*/