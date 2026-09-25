#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int dfs(
    int k,
    const vector<vector<int>>& dungeons,
    vector<bool>& visited
) {
    int maxCnt = 0;

    for(int i = 0; i < dungeons.size(); i++) {

        if(!visited[i] && k >= dungeons[i][0]) {

            visited[i] = true;

            maxCnt = max(
                maxCnt,
                1 + dfs(
                    k - dungeons[i][1],
                    dungeons,
                    visited
                )
            );

            visited[i] = false;
        }
    }

    return maxCnt;
}

int solution(int k, vector<vector<int>> dungeons) {
    vector<bool> visited(dungeons.size(), false);

    return dfs(k, dungeons, visited);
}