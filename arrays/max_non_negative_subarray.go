package main

import ( 
	"fmt" 
)

func min(x, y int) int {
    if (x < y) {
        return x;
    }
    return y;
}

/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
 func maxset(A []int )  ([]int) {
    
    arr_len := len(A)
    max_begin, max_end := -1, -1
    max_sum := 0
    
    begin, end := 0, 0
    arr_sum := 0
    
    for ; end < arr_len; {
        if (A[end] >= 0) {
            arr_sum += A[end];
        } else {
            end++;
            begin = end;
            arr_sum = 0;
            continue;
        }

        if (arr_sum == max_sum) {
           if (end - begin > max_end - max_begin) {
               max_end = end;
               max_begin = begin;
           }
        } else if (arr_sum > max_sum) {
            max_end = end;
            max_begin = begin;
            max_sum = arr_sum;
        }
        end+=1;
    }

    if max_begin == -1 && max_end == -1 {
        return []int{}
    }
    return A[max_begin : min(max_end + 1, arr_len)];
}

func main() {
	fmt.Println(maxset([]int{ -1, -1, -1, -1, -1 }))
}