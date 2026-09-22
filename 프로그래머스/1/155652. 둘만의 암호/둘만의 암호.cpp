#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    
    for(char c : s){
        int cnt = 0;
        char cur = c;
        while(cnt < index){
            cur = (char)((int)cur + 1);
            if(cur > 'z')
                cur = 'a';
            if(skip.find(cur) == string::npos){  
                cnt ++;
            }
        }
        answer += cur;
    }
    
    return answer;
}