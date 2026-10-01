#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    
    unordered_map<int, int> in_map;
    unordered_map<int, int> el_map;
    
    for (string record : records) {
        int hour = stoi(record.substr(0, 2));
        int minute = stoi(record.substr(3, 2));
        int number = stoi(record.substr(6, 4));
        string type = record.substr(11);
        
        int time = hour * 60 + minute;
        
        if (type == "OUT") {
            el_map[number] += time - in_map[number];
            in_map[number] = -1;
        } 
        else {
            in_map[number] = time;
        }
    }
    
    vector<pair<int, int>> v(in_map.begin(), in_map.end());
    sort(v.begin(), v.end());
    
    for (auto [number, in_time] : v) {
        int elapse = el_map[number];
        
        if (in_time != -1) {
            elapse += 23 * 60 + 59 - in_time;
        }

        int default_time = fees[0];
        int default_price = fees[1];
        int unit_time = fees[2];
        int unit_price = fees[3];
        
        int final_price = default_price;
        
        if (elapse > default_time) {
            int extra = elapse - default_time;
            final_price += 
                ((extra + unit_time - 1) / unit_time) * unit_price;
        }
        
        answer.push_back(final_price);
    }
    
    return answer;
}