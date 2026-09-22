#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    vector<int> answer;
    
    vector<int> rowArr;
    vector<int> colArr;
    
    for(int i = 0 ; i < wallpaper.size() ; i++){
        for(int j = 0 ; j < wallpaper[i].size() ; j++){
            if(wallpaper[i][j] == '#'){
                rowArr.push_back(i);
                colArr.push_back(j);
            }
        }
    }
    
    int maxRow = *std::max_element(rowArr.begin(), rowArr.end());
    int minRow = *std::min_element(rowArr.begin(), rowArr.end());
    int maxCol = *std::max_element(colArr.begin(), colArr.end());
    int minCol = *std::min_element(colArr.begin(), colArr.end());
    
    
    // cout << maxRow << minRow << maxCol << minCol << endl;
    answer = {minRow, minCol, maxRow + 1, maxCol + 1};
    
    return answer;
}