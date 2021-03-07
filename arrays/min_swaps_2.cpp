int Solution::solve(vector<int> &A, int B) {
    int q = 0, total_less_than_b = 0;
    int l = A.size();
    
    for(; q < l; q++) {
        if (A[q] <= B) total_less_than_b++;
    }
    
    int min_swaps = INT_MAX, cur_swaps = 0;
    q = 0;
    
    while (q < l) {
        if (q < total_less_than_b) {
            if (A[q] > B) cur_swaps++;
        } else {
            if (A[q] > B) {
                cur_swaps++;
            }
            if (A[q - total_less_than_b] > B) {
                cur_swaps--;
            }
            
            min_swaps = min(min_swaps, cur_swaps);
        }
        q++;
    }
    
    return min(min_swaps, cur_swaps);
}
