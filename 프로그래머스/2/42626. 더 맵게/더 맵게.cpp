#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for(int item:scoville){
        pq.push(item);
    }
    
    int cnt = 0;
    while(true){
        int s1 = pq.top();
        pq.pop();
        
        if(s1 >= K){
            break;
        }
        
        if(pq.empty()){
            return -1;
        }
        
        int s2 = pq.top();
        pq.pop();
        
        int newS = s1 + s2 * 2;
        
        pq.push(newS);
        
        cnt += 1;
    }
    
    answer = cnt;
    
    return answer;
}