/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
 
int bin_search(vector<Interval> &a, Interval &in, int l, int r) {
    if (l == r) return l;
    
    int mid = (l + r)/2;
    if (in.start > a[mid].start) {
        return bin_search(a, in, mid + 1, r);
    } else if (in.start < a[mid].start) {
        return bin_search(a, in, l, mid);
    } else {
        return mid;
    }
} 
 
vector<Interval> Solution::insert(vector<Interval> &intervals, Interval newInterval) {
    
    int vec_len = intervals.size();
    vector<Interval> v;

    if (vec_len < 1) {
        v.push_back(newInterval);
        return v;
    }

    if (newInterval.start <= intervals[0].start) { 
        intervals.insert(intervals.begin(), newInterval);
    }
    else if (newInterval.start >= intervals[vec_len - 1].start) {
        intervals.push_back(newInterval);
    }
    else { 
        int pos = bin_search(intervals, newInterval, 0, intervals.size()); 
        intervals.insert(intervals.begin() + pos, newInterval);
    }
    
    int min_start = intervals[0].start, max_end = intervals[0].end, i = 0; 
    for (; i < vec_len + 1; i++) {
        if (intervals[i].start > max_end) {
            v.push_back({ min_start, max_end });
            min_start = intervals[i].start;
            max_end = intervals[i].end;
        }
        min_start = min(intervals[i].start, min_start);
        max_end = max(intervals[i].end, max_end);
    }
    v.push_back({ min_start, max_end });
    return v;
}
