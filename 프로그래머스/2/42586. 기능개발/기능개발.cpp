#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    int maxDue = -1;
    int last = -1;

    for(int i = 0; i < progresses.size(); i++) {

        int due = (100 - progresses[i] + speeds[i] - 1) / speeds[i];

        if(due > maxDue) {
            maxDue = due;

            if(last != -1) {
                answer.push_back(i - last);
            }

            last = i;
        }
    }

    answer.push_back(progresses.size() - last);

    return answer;
}