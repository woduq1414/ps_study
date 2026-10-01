#include <string>
#include <vector>

using namespace std;

vector<vector<int>> user_list;
vector<int> emoticon_list;

int max_register;
int max_revenue;

void dfs(int cnt, vector<int>& cur) {
    
    if(cnt == 0) {
        int reg_count = 0;
        int revenue = 0;
        
        for(int i = 0; i < user_list.size(); i++) {
            int sum = 0;
            
            for(int j = 0; j < cur.size(); j++) {
                
                if(cur[j] >= user_list[i][0]) {
                    sum += emoticon_list[j]
                         * (100 - cur[j]) / 100;
                }
            }
            
            if(sum >= user_list[i][1]) {
                reg_count++;
            } else {
                revenue += sum;
            }
        }
        
        if(reg_count > max_register ||
           (reg_count == max_register && revenue > max_revenue)) {
            
            max_register = reg_count;
            max_revenue = revenue;
        }
        
        return;
    }
    
    for(int discount = 10; discount <= 40; discount += 10) {
        cur.push_back(discount);
        
        dfs(cnt - 1, cur);
        
        cur.pop_back();
    }
}

vector<int> solution(vector<vector<int>> users,
                     vector<int> emoticons) {
    
    user_list = users;
    emoticon_list = emoticons;

    max_register = 0;
    max_revenue = 0;
    
    vector<int> cur;
    
    dfs(emoticons.size(), cur);
    
    return {max_register, max_revenue};
}