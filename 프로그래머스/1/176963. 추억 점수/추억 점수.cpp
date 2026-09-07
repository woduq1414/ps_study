#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    
    map<string, int> dict;
    for(int i = 0 ; i < name.size() ; i++){
        dict[name[i]] = yearning[i];
    }
    
    for(vector<string> p : photo){
        int s = 0;
        for(string name : p){
            s += dict[name];
        }
        answer.push_back(s);
    }
    

    
    return answer;
}