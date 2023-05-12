#include <string>
#include <vector>

using namespace std;




int solution(string s) {
    int answer = 0;
    
    char fc = NULL;
    int fc_cnt = 0;
    int other_cnt = 0;
    for(int i = 0; i < s.length() ; i ++){
        if(fc == NULL){
            fc = s[i];
            fc_cnt = 1;
            other_cnt = 0;
        }else{
            if(fc == s[i]){
                fc_cnt += 1;
            }else{
                other_cnt += 1;
            }
        }
        if(fc_cnt == other_cnt){
            answer += 1;
            fc = NULL;
        }
    }   
    if(fc != NULL){
        answer += 1;
    }

    
    return answer;
}