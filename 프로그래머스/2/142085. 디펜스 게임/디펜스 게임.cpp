#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(int n, int k, vector<int> enemy) {
    priority_queue<int, vector<int>, greater<int>> pq;
    
    int hp = n;
    int i = 0;
    for(i = 0 ; i < enemy.size(); i++){
        int e = enemy[i];
        if(pq.size() < k){
            pq.push(e);
        }else{
            int top = pq.top();
            if(e > top){
                pq.pop();
                pq.push(e);
                hp -= top;
            }else{
                hp -= e;
            }
        }
         // cout << i << " " << hp << endl;
        if(hp < 0){
            break;
        }
        
       
    }
    
    int answer = i;
    return answer;
}