#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    
    unordered_map<char, int> mp;
    
    for(string keystr: keymap){
        for(int i = 0 ; i < keystr.length(); i++){
            char c = keystr[i];
            
            if(mp.contains(c)){
                mp[c] = min(mp[c], i + 1);
            }else{
                mp[c] = i + 1;
            }
            
        }
    }
    
    
    for(string target : targets){
        int s = 0;
        for(char c :target){
            if(mp.contains(c)){
                s += mp[c];
            }else{
                s = -1;
                break;
            }
            
        }
        answer.push_back(s);
        
    }
    
    return answer;
}