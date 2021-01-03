class Solution {
public:
    int minArray(vector<int>& numbers) {
        if (numbers.size() == 0) return 0;
        numbers.push_back(numbers[0]);

        for (int i = 0; i < numbers.size(); ++i) {
            if (i > 0 && numbers[i] < numbers[i-1]) return numbers[i];
        }

        return numbers[numbers.size()-1];
    }
};
