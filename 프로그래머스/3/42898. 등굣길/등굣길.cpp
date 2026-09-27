#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    vector<vector<int>> pd(n + 1, vector<int>(m + 1, 0));
    
    for(auto& puddle : puddles){
        pd[puddle[1]][puddle[0]] = 1;
    }
    
    dp[1][1] = 1;
    
    for(int i = 1 ; i <= n ; i ++){
        for (int j = 1 ; j <= m ; j ++){
            if(pd[i - 1][j] == 0){
                dp[i][j] += dp[i - 1][j];
            }
            if(pd[i][j - 1] == 0){
                dp[i][j] += dp[i][j - 1];
            }
            dp[i][j] = dp[i][j] % 1000000007;
        }
    }
    
    // for(int i = 1 ; i <= n ; i ++){
    //     for (int j = 1 ; j <= m ; j ++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    
    answer = dp[n][m];
    
    return answer;
}