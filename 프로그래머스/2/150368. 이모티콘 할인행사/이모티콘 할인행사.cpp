#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> user_list;

vector<int> emoticon_list;
int max_register = 0;
int max_revenue = 0;

void dfs(int cnt, vector<int> cur){
    
    if(cnt == 0){
        // for(int i = 0; i < cur.size(); i++){
        //     cout << cur[i] << " ";
        // }
        // cout << endl;
        
        int reg_count = 0;
        int revenue = 0;
        
        for(int i = 0 ; i < user_list.size(); i++){
            int s = 0;
            for(int j = 0 ; j < cur.size(); j++){
            
                if(cur[j] >= user_list[i][0]){
                    s += emoticon_list[j] * (100 - cur[j]) / 100;
                }
            }
            // cout<< i << " " << reg_count << " " << s << endl;
            if(s >= user_list[i][1]){
                reg_count += 1;
            }else{
                revenue += s;
            }
        }
        // cout << reg_count << " " << revenue << endl;
        if(reg_count > max_register ||  (reg_count == max_register && revenue >= max_revenue)){
               
            
            max_register = reg_count;
            max_revenue = revenue;
        }
        
        
        
        return;
    }
    
    for(int i = 10; i <= 40; i += 10){
        cur.push_back(i);
        dfs(cnt - 1, cur);
        cur.pop_back();
    }
    
}



vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    vector<int> answer;
    user_list = users;
    emoticon_list = emoticons;
    int emoticon_count = emoticons.size();
    vector<int> cur = {};
    
    vector<int> d = {10, 20, 30, 40};
    
    dfs(emoticon_count, cur);
    
    answer = {
        max_register, max_revenue
        };
    
    return answer;
}