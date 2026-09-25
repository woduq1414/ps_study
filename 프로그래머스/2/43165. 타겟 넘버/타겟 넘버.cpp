#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    unordered_map<int, int> mp;
    mp[0] = 1;
    for(int i = 0 ; i < numbers.size() ; i++){
        unordered_map<int, int> newMap;
        for(auto& item : mp){
            if(item.first + numbers[i] <= 2000){
                newMap[item.first + numbers[i]] += item.second;
            }
            if(item.first + numbers[i] >= -1000){
                newMap[item.first - numbers[i]] += item.second;
            }
            
        }
        
        mp = newMap;
    }
    
    answer = mp[target];
    
    
    return answer;
}