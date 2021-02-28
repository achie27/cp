/**
* @input A : Integer array
* 
* @Output Integer array.
*/
package main

import ( 
	"sort"
	"fmt" 
)

func wave(A []int )  ([]int) {
	sort.Ints(A)
	
	arr_len := len(A)
	for i := 0; i < arr_len; i += 2 {
		if i + 1 < arr_len {
			A[i], A[i+1] = A[i + 1], A[i]   
		}
	}
	
	return A;
}

func main() {
	fmt.Println(wave([]int{3, 1, 2}))
}

