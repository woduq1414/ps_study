#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<string> board) {
    int H = board.size();
    int W = board[0].size();

    int sr, sc;

    for (int r = 0; r < H; r++) {
        for (int c = 0; c < W; c++) {
            if (board[r][c] == 'R') {
                sr = r;
                sc = c;
            }
        }
    }

    vector<vector<int>> dist(H, vector<int>(W, -1));
    queue<pair<int, int>> q;

    q.push({sr, sc});
    dist[sr][sc] = 0;

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (board[r][c] == 'G')
            return dist[r][c];

        for (int d = 0; d < 4; d++) {
            int nr = r;
            int nc = c;

            while (true) {
                int tr = nr + dr[d];
                int tc = nc + dc[d];

                if (tr < 0 || tr >= H || tc < 0 || tc >= W)
                    break;

                if (board[tr][tc] == 'D')
                    break;

                nr = tr;
                nc = tc;
            }

            if (dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    return -1;
}