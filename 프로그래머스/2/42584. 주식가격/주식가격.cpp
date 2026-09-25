#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size());
    fill(answer.begin(), answer.end(), 0);
    
    vector<pair<int, int>> stack;
    
    for(int i = 0 ; i < prices.size() ; i++){
        
        for(int j = stack.size() - 1 ; j >= 0 ; j --){
            auto& item = stack[j];
            if(prices[i] < item.first){
                answer[item.second] = i - item.second;
                
                stack.pop_back();
            }else{
                break;
            }
        }
        
        stack.push_back({prices[i], i});
        
    }
    
    for(auto& item : stack){
        answer[item.second] = prices.size() - item.second - 1;
    }
    
    return answer;
}