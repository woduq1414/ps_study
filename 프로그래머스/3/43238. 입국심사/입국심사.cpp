#include <string>
#include <vector>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    
    long long left = 0;
    long long right = 1000000000LL * 1000000000LL; 
    long long mid;
    
    while(left <= right){
        mid = (left + right) / 2;
        
        long long s = 0;
        for(int i = 0 ; i < times.size(); i ++){
            s += mid / times[i];
        }
        // cout << s << endl;
        
        if(s >= n){
            right = mid - 1;
        }else{
            left = mid + 1;
        }
    }
    // cout << left << " " << mid << " " << right << endl;
    return left;
   
}