#include <string>
#include <vector>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "";
    
    int pos1 = 0;
    int pos2 = 0;
    int goalPos = 0;
    
    for(int i = 0; i < goal.size(); i++){
        string goalWord = goal[i];
        string card1 = "";
        string card2 = "";
        
        if(pos1 < cards1.size()){
            card1 = cards1[pos1];
        }
        if(pos2 < cards2.size()){
            card2 = cards2[pos2];
        }

        
        if(goalWord == card1){
            pos1++;
        }else if(goalWord == card2){
            pos2++;
        }else{
            return "No";
        }
    }
    
    return "Yes";
}