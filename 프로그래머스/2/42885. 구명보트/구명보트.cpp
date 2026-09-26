#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    sort(people.begin(), people.end());
    
    int left = 0;
    int right = people.size() - 1;
    int cnt = 0;
    while(left <= right){
        if(people[left] + people[right] <= limit){
            left++;
            right--;
        }else{
            right--;
        }
        cnt++;
    }
    answer = cnt;
    return answer;
}