#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string solution(string X, string Y) {
    string answer = "";
    
    int arrX[10] = {0};
    int arrY[10] = {0};
    for(char c : X){
        arrX[c - '0'] += 1;
    }
    for(char c : Y){
        arrY[c - '0'] += 1;
    }
    
    
    int minNum = -1;
    for(int i = 9 ; i >= 0 ; i--){
        int repeat = min(arrX[i], arrY[i]);
        if(repeat >= 1 && minNum == -1){
            minNum = i;
        }
        for(int j = 0 ; j < repeat ; j ++){
            answer += i + '0';
        }
    }
    
    
    
    if(minNum == -1){
        return "-1";
    }else if(minNum == 0){
        return "0";
    }
    else{
        return answer;
    }
    
    
    return answer;
}