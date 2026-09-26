#include <vector>
#include <algorithm>
#include <climits>
#include <cstdlib>

using namespace std;

int answer;

int dfs(
    int node,
    int parent,
    int n,
    const vector<vector<int>>& graph
) {
    int subtreeSize = 1;

    for(int next : graph[node]) {

        // 부모로 다시 돌아가지 않음
        if(next == parent)
            continue;

        int childSize = dfs(
            next,
            node,
            n,
            graph
        );

        // node - next 간선을 끊는 경우
        int diff = abs(
            childSize - (n - childSize)
        );

        answer = min(answer, diff);

        subtreeSize += childSize;
    }

    return subtreeSize;
}

int solution(int n, vector<vector<int>> wires) {
    vector<vector<int>> graph(n + 1);

    for(auto& wire : wires) {
        int a = wire[0];
        int b = wire[1];

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    answer = INT_MAX;

    dfs(1, -1, n, graph);

    return answer;
}