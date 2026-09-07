#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer;
    
    pair<int, int> curPos;
    for(int i = 0 ; i < park.size(); i ++){
        string row = park[i];
        int sPos = row.find("S");
        if(sPos >= 0){
            curPos = {
                i,sPos
            };
        }
    } 
    int w = park[0].length();
    int h = park.size();
 
    for(string route : routes){
        string dir = route.substr(0, 1);
        int mag = stoi(route.substr(2, route.length()));
        
        bool f = true;
        
        pair<int, int> dirPair;
        pair <int, int> newPos;
        if(dir == "E"){
            dirPair = {0, 1};
        }else if(dir == "W"){
            dirPair = {0, -1};
        }else if(dir == "S"){
            dirPair = {1, 0};
        }else if(dir == "N"){
            dirPair = {-1, 0};
        }
        
        for(int i = 1 ; i <= mag ; i ++){
            newPos = {
                curPos.first + dirPair.first * i, curPos.second + dirPair.second * i
            };
            cout << newPos.first << " z" << newPos.second << endl;
            
            if(0 <= newPos.first && newPos.first < h && 0 <= newPos.second && newPos.second < w){
                if(park[newPos.first][newPos.second] == 'X'){
                    f = false;
                    break;
                }
            }else{
                f = false;
                break;
            }
            
            
        
            
        }
        if(f == true){
            curPos = newPos;
        }
        
        // cout << curPos.first << " " << curPos.second << endl;
        
    }
    
    answer.push_back(curPos.first);
    answer.push_back(curPos.second);
    
    return answer;
}