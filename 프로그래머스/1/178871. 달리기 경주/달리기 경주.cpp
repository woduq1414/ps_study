#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    
    map<string, int> rankDict;
    map<int, string> reverseRankDict;
    
    for(int i = 0; i < players.size() ; i++){
        rankDict[players[i]] = i;
        reverseRankDict[i] = players[i];
    }

    for(int i = 0 ; i < callings.size(); i++){
        string calling = callings[i];
        int currentRank = rankDict[calling];
        string priorPlayer = reverseRankDict[currentRank - 1];
        
        rankDict[calling] = currentRank - 1;
        rankDict[priorPlayer] = currentRank;
        reverseRankDict[currentRank] = priorPlayer;
        reverseRankDict[currentRank - 1] = calling;

    }
    
    vector<pair<int, string>> v;

    for (auto [key, value] : rankDict) {
        v.push_back({value, key});
    }

    sort(v.begin(), v.end());

    for (auto [value, key] : v) {
        answer.push_back(key);
    }
    
        

  

    
    return answer;
}