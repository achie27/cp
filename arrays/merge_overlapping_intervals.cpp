/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
vector<Interval> Solution::merge(vector<Interval> &A) {
    sort(A.begin(), A.end(), [](Interval p, Interval q) -> bool{
        if (p.start < q.start) return true;
        if (p.start == q.start) {
            return p.end < q.end;
        }
        
        return false;
    });

    struct Interval cur = {A[0].start, A[0].end};
    vector<Interval> res;
    
    for (int i = 0, l = A.size(); i < l; i++) {
        if (cur.end >= A[i].start) {
            cur.end = max(A[i].end, cur.end);
            cur.start = min(cur.start, A[i].start);
        } else {
            res.push_back(cur);
            cur.end = A[i].end;
            cur.start = A[i].start;
        }
    }
    
    res.push_back(cur);
    return res;
}
