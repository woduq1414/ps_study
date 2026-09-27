#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int N, int number) {
    int answer = -1;

    vector<vector<int>> dp(9);

    dp[1] = {N};

    dp[2] = {
        N + N,
        N * N,
        N * 11,
        1
    };

    for(int i = 1; i <= 2; i++) {
        for(int j = 0; j < dp[i].size(); j++) {
            if(dp[i][j] == number) {
                return i;
            }
        }
    }

    int concat = N * 11;

    for(int i = 3; i <= 8; i++) {

        // NNN, NNNN, ...
        concat = concat * 10 + N;
        dp[i].push_back(concat);

        // dp[i-1] 과 N 조합
        for(int j = 0; j < dp[i - 1].size(); j++) {

            int a = dp[i - 1][j];

            dp[i].push_back(a + N);
            dp[i].push_back(a * N);

            // 순서가 중요한 연산
            dp[i].push_back(a - N);
            dp[i].push_back(N - a);

            dp[i].push_back(a / N);

            if(a != 0) {
                dp[i].push_back(N / a);
            }
        }

        // dp[j] 와 dp[i-j] 조합
        for(int j = 2; j <= i / 2; j++) {

            for(int k = 0; k < dp[j].size(); k++) {
                for(int l = 0; l < dp[i - j].size(); l++) {

                    int a = dp[j][k];
                    int b = dp[i - j][l];

                    dp[i].push_back(a + b);
                    dp[i].push_back(a * b);

                    // 두 방향 모두
                    dp[i].push_back(a - b);
                    dp[i].push_back(b - a);

                    if(b != 0) {
                        dp[i].push_back(a / b);
                    }

                    if(a != 0) {
                        dp[i].push_back(b / a);
                    }
                }
            }
        }

        vector<int> tmp;

        for(int item : dp[i]) {

            if(item == number) {
                return i;
            }

            // 네 방식대로 0 제거
            if(item != 0) {
                tmp.push_back(item);
            }
        }

        dp[i] = tmp;
    }

    return -1;
}