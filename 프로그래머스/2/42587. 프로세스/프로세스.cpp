#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    int isPop[100] = {0};
    int delta = 0;
    int cnt = 0;
    while(true){
        cnt++;
        int maxIdx = delta;
        for(int i = 0; i < priorities.size(); i++){
            int di = (delta + i) % priorities.size();
            if(priorities[di] > priorities[maxIdx] && isPop[di] == 0){
                maxIdx = di;
            }
        }
        cout << maxIdx << endl;
        if(maxIdx == location){
            return cnt;
        }
        
        isPop[maxIdx] = 1;
        
        delta = maxIdx;
        do{
            delta = (delta + 1) % priorities.size();
        }while(isPop[delta] == 1);
        
        
        
    }
    
    return answer;
}