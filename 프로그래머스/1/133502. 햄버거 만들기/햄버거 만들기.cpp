#include <string>
#include <vector>

using namespace std;

int solution(vector<int> ingredient) {
    int answer = 0;
    
    vector<int> stack;
    for(int item : ingredient){
        if(item != 1){
            stack.push_back(item);    
        }else{
            if(stack.size() >= 3 && stack[stack.size() - 1] == 3 && stack[stack.size() - 2] == 2 && stack[stack.size() - 3] == 1){
                stack.pop_back();
                stack.pop_back();
                stack.pop_back();
                answer += 1;
            }else{
                stack.push_back(item);
            }
        }
        
    }
    
    return answer;
}