#include <string>
#include <vector>
#include <iostream>

using namespace std;

int dfs(int k, vector<vector<int>> dungeons, vector<bool> visited){
    int maxCnt = -1;
    for(int i = 0 ; i < dungeons.size() ; i++){
        if(!visited[i]){
            vector<int> dungeon = dungeons[i];
            if(k >= dungeon[0] ){
                visited[i] = true;
                
                maxCnt = max(maxCnt, dfs(k - dungeon[1], dungeons, visited ));
                visited[i] = false;
            }
        }
    }
    return maxCnt + 1;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    vector<bool> visited(dungeons.size(), false);
    
    answer = dfs(k, dungeons, visited);
    
    return answer;
}