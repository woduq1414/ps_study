#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    
    unordered_map<int, int> in_map;
    unordered_map<int, int> el_map;
    
    
    for(string record: records){
        int hour = stoi(record.substr(0, 2));
        int minute = stoi(record.substr(3, 5));
        int number = stoi(record.substr(6, 10));
        string type = record.substr(11,13);
        
        if(type == "OUT"){
            int elapse;
            if(in_map.contains(number)){
                elapse = hour * 60 + minute - in_map[number];
            }
            el_map[number] += elapse;
            in_map[number] = -1;
        }else{
            in_map[number] = hour * 60 + minute;
            
        }
    }
    
    
    
    vector<pair<int, int>> v(in_map.begin(), in_map.end());
    sort(v.begin(), v.end());
    for(auto item: v){
        int number = item.first;
        int elapse = el_map[number];
        
        if(in_map[number] != -1){
            elapse += 23 * 60 + 59 - in_map[number];
        }

        int default_time = fees[0];
        int default_price = fees[1];
        int unit_time = fees[2];
        int unit_price = fees[3];
        
        int final_price;
        if(elapse <= default_time){
            final_price = default_price;
        }else{
            final_price = default_price + ceil((elapse - default_time) / (double)unit_time) * unit_price;
        }
        
        answer.push_back(
            final_price
        );
    }
    
    
    return answer;
}