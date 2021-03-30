double Solution::findMedianSortedArrays(const vector<int> &A, const vector<int> &B) {
    
    int m = A.size(), n = B.size();

    if (m > n) return findMedianSortedArrays(B, A);

    int imin, imax, i, j; 
    // A allocation min
    imin = 0;
    // A allocation max
    imax = m;

    while (imin <= imax) {
        // current length allocated to A
        i = (imin + imax)/2;

        // corresponding length allocated to B
        j = (m+n+1)/2 - i;

        // B's last allocated element is greater than A's next element
        // eg -
        // A = [4, 20, 32, 50, 55, 61]
        // B = [1, 15, 22, 30, 70]
        // For i = 1, B[4] > A[1] i.e 70 > 20 
        if (j > 0 && i < m && B[j - 1] > A[i]) {
            // This means, these elements (A[0, i] union B[0, j]) don't make up the first half elements of the combined array
            // since there exists an element (A[i]) which is not in the union but lesser than the max element of B
            // We now need to ensure that A[i] is included in the union
            imin = i + 1;
        } else if (i > 0 && j < n && A[i - 1] > B[j]) {
            // Same as the above but with different arrays
            imax = i - 1;
        } else {
            // We've now found the allocation for the first half of A union B
            // Figure out median now. 
            int median1 = 0, median2 = 0;

            // All A's elements are greater than B's elements
            if (i == 0) {
                median1 = B[j - 1];
            }
            // All B's elements are greater than A's elements
            else if (j == 0) {
                median1 = A[i - 1];
            }
            // The would-be last element of this configuration is (a) median
            else {
                median1 = max(A[i - 1], B[j - 1]);
            }

            // For odd total length, this is the answer
            if ((m+n) % 2 == 1) {
                return 1.0 * median1;
            }

            // To find the second median when total length is even
            // we need to find the element just greater than median1

            // In case all of A is in the allocation, the max can only be the next elem in B's allocation
            if (i == m) {
                median2 = B[j];
            }
            // In case all of B is in the allocation, the max can only be the next elem in A's allocation
            else if (j == n) {
                median2 = A[i];
            }
            // Whichever is lesser will come after the last elem of the allocation
            else {
                median2 = min(A[i], B[j]);
            }
            return 1.0 * (median1 + median2) / 2.0;
        }
    }
}