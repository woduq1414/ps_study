#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    unordered_map<string,int> m;
    for(string c : completion){
        if(m.contains(c)){
            m[c] += 1;
        }else{
            m[c] = 1;
        }
    }
    for(string p : participant){
        if(!m.contains(p)){
            return p;
        }else{
            m[p] -= 1;
        }
    }
    for(auto& pair : m){
        if(pair.second != 0){
            return pair.first;
        }
    }
    
    
    return answer;
    
    
}