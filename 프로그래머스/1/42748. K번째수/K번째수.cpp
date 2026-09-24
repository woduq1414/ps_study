#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(vector<int> command : commands){
        vector<int> subArr;
        for(int i = command[0] -1 ; i < command[1] ; i ++ ){
            subArr.push_back(array[i]);
        }
        sort(subArr.begin(), subArr.end());
        answer.push_back(subArr[command[2] - 1]);
    }
    
    
    return answer;
}