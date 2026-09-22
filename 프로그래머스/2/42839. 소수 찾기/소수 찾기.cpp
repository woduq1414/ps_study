
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool isPrime(int number);

void func(string current, string remain){
    
}


int solution(string numbers) {
    int answer = 0;
    
    vector<int> v;
    for (int i = 0 ; i < numbers.size(); i++){
        v.push_back(numbers[i]);
    }
    
    sort(v.begin(), v.end());
    do {
        for (auto it = v.begin(); it != v.end(); ++it)
            cout << *it << ' ';
        cout << endl;
    } while (next_permutation(v.begin(), v.end()));
     
        
    
    return answer;
}


bool isPrime(int number){
    if(number <= 1){
        return false;
    }
    
    bool f = true;
    for(int i = 2 ; i * i <= number ; i++){
        if(number % i == 0){
            f = false;
            break;
        }
    }
    return f;
}