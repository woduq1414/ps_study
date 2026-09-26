#include <string>
#include <vector>

using namespace std;

void dfs(int node, const vector<vector<int>>& computers, vector<bool>& visited){
    for(int i = 0 ; i < computers.size() ; i++){
        if(!visited[i] && computers[node][i] == 1 && i != node){
            visited[i] = true;
            dfs(i, computers, visited);
            // visited[i] = false;
        }
    }

}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    vector<bool> visited(n, false);
    
    int cnt = 0;
    for(int i = 0 ; i < n ; i ++){
        if(visited[i] == false){
            dfs(i, computers, visited);
            cnt += 1;
        }
    }
    answer = cnt;
    
    return answer;
}