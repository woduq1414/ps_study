#include <vector>
#include <queue>

using namespace std;

int solution(vector<vector<int>> maps)
{
    int n = maps.size();
    int m = maps[0].size();

    queue<pair<int, int>> q;
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    int dirs[4][2] = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    q.push({0, 0});
    visited[0][0] = true;

    int dist = 1;

    while(!q.empty()) {

        int qSize = q.size();

        // 현재 거리(dist)에 있는 칸들을 전부 처리
        for(int i = 0; i < qSize; i++) {

            auto [r, c] = q.front();
            q.pop();

            if(r == n - 1 && c == m - 1) {
                return dist;
            }

            for(auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if(nr < 0 || nr >= n ||
                   nc < 0 || nc >= m) {
                    continue;
                }

                if(visited[nr][nc])
                    continue;

                if(maps[nr][nc] == 0)
                    continue;

                visited[nr][nc] = true;
                q.push({nr, nc});
            }
        }

        // 한 레벨을 다 처리한 뒤에만 +1
        dist++;
    }

    return -1;
}