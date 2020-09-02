class MedianFinder {
public:
    /** initialize your data structure here. */
    priority_queue<long> small, big;
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        small.push(num);
        big.push(-small.top());
        small.pop();
        if (small.size() < big.size()) {
            small.push(-big.top());
            big.pop();
        }
        //if (small.size() <= big.size()) small.push(num);
        //else big.push(-num);
    }
    
    double findMedian() {
        return small.size() > big.size() ? small.top() : 0.5 * (small.top() - big.top());
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
