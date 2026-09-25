#include<string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<char> st;
    for(char c:s){
        if(c == '('){
            st.push_back('(');
        }else if(c == ')'){
            if(st.size() > 0 && st[st.size() - 1] == '('){
                st.pop_back();    
            }else{
                return false;
            }
        }
    }
    if(st.size() == 0){
        answer = true;
    }else{
        answer = false;
    }
    
    return answer;
}