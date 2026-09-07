#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    
    int curIdx = 0;
    int cnt = 0;
    
    while(curIdx < section.size()){
        int curPos = section[curIdx];
        int endCoverPos = curPos + m - 1;
        
        curIdx = upper_bound(section.begin(), section.end(), endCoverPos) - section.begin();
        
       
        cnt++;
    }
    
    answer = cnt;
    
    
    return answer;
}