package main

import ( 
	"fmt" 
)

func main() {
	fmt.Println(subUnsort([]int{1, 3, 2, 4, 5}))
}
func max(a, b int) int {
    if a > b {
        return a
    }
    
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    
    return b
}

/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
func subUnsort(A []int )  ([]int) {
    p, q, n := 0, len(A) - 1, len(A)

    for ; p < n - 1; {
        if A[p] > A[p + 1] {
            break
        }
        p++
    }

    for ; q > 0; {
        if A[q] < A[q - 1] {
            break
        }
        q--
    }
    
    if p == n - 1 && q == 0 {
        return []int{-1}
    }
    
    mn, mx := A[p], A[p]
    for i := p; i <= q; i++ {
        mn = min(mn, A[i])
        mx = max(mx, A[i])
    }
    
    l, r := 0, n-1
    for ; l < p && mn >= A[l]; {
        l++
    }
    
    for ; r > q && mx <= A[r]; {
        r--
    }
    
    return []int{l, r}
}