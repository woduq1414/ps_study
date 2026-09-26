#include <string>
#include <vector>
#include <iostream>

using namespace std;

int dfs(int node, const vector<vector<int>>& arr, vector<bool>& visited, int cnt){
    visited[node] = true;
    
    // cout << node << endl;
    for(int i = 1 ; i <= arr.size() ; i ++){
        if(!visited[i] && arr[node][i] == 1){
            cnt = dfs(i, arr, visited, cnt + 1);
        }
    }
    
    return cnt;
    
}


int solution(int n, vector<vector<int>> wires) {
    int m = -1;
    vector<vector<int>> arr(n + 1, vector<int>(n + 1, 0));
    for(int i = 0; i < n - 1 ; i ++){
        vector<int> wire = wires[i];
        arr[wire[0]][wire[1]] = 1;
        arr[wire[1]][wire[0]] = 1;
    }
    for(int i = 0 ; i < n - 1 ; i ++){
        vector<int> wire = wires[i];
        arr[wire[0]][wire[1]] = 0;
        arr[wire[1]][wire[0]] = 0;
        
        vector<bool> visited(n + 1, false);
        int cnt = dfs(wire[0], arr, visited, 1);
        cnt = min(cnt, n - cnt);
     
        if(cnt > m){
            m = cnt;
        }
        
        arr[wire[0]][wire[1]] = 1;
        arr[wire[1]][wire[0]] = 1;
    }
    
    
    
    int answer = n - 2 * m;
    return answer;
}