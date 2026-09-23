#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    int arr[26] = {};
    for(int i = 0 ; i < 26 ; i++){
        arr[i] = -1;
    }
    
    for(int i = 0 ; i < s.size() ; i++){
        int cur = s[i] - 'a';
        if(arr[cur] == -1){
            answer.push_back(-1);
        }else{
            answer.push_back(i - arr[cur]);
        }
        arr[cur] = i;
    }
    
    return answer;
}