#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    
    vector<vector<int>> dp(2, vector<int>(triangle.size() + 2, 0));

    for(int i = 0 ; i < triangle.size(); i++){
        vector<int> row = triangle[i];
        for(int j = 1 ; j <= row.size(); j++){
            dp[i % 2][j] = max(dp[(i + 1) % 2][j - 1], dp[(i + 1) % 2][j]) + row[j - 1];
        }
    }
 
    return *max_element(dp[(triangle.size() + 1) % 2].begin(), dp[(triangle.size() + 1) % 2].end());
    
    return answer;
}