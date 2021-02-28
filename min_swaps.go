package main

import ( 
	"fmt" 
)

func main() {
	fmt.Println(solve([]int{1, 2, 3, 4, 0}))
}

/**
 * @input A : Integer array
 * 
 * @Output Integer
 */
 func solve(A []int )  (int) {
    cur_elem_pos := make([]int, len(A))
    for i := 0; i < len(A); i++ {
        cur_elem_pos[A[i]] = i
    }
    
    swaps := 0
    for i := 0; i < len(A); i++ {
		fmt.Println(i, cur_elem_pos, A)

        if A[i] != i {
            swaps++
            
            arr_pos_i := cur_elem_pos[i]

            cur_elem_pos[i] = i
            cur_elem_pos[A[i]] = arr_pos_i
            
            A[arr_pos_i] = A[i]
            A[i] = i

        }
    }

	fmt.Println("last", cur_elem_pos, A)
    
    return swaps
}
