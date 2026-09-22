#include <string>
#include <set>
using namespace std;

bool isPrime(int number) {
    if (number <= 1) {
        return false;
    }

    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return false;
        }
    }

    return true;
}

void func(string current, string remain, set<int>& result) {
  
    if (!current.empty()) {
        int number = stoi(current);

        if (isPrime(number)) {
            result.insert(number);
        }
    }

    for (int i = 0; i < remain.size(); i++) {
        string nextCurrent = current + remain[i];

        string nextRemain = remain.substr(0, i)
                          + remain.substr(i + 1);

        func(nextCurrent, nextRemain, result);
    }
}

int solution(string numbers) {
    set<int> result;

    func("", numbers, result);

    return result.size();
}