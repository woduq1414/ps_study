#include <string>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int toMinute(string time) {
    return stoi(time.substr(0, 2)) * 60
         + stoi(time.substr(3, 2));
}

vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;

    stack<pair<string, int>> st;

    sort(plans.begin(), plans.end(),
         [](const auto& a, const auto& b) {
             return a[1] < b[1];
         });

    for (int i = 0; i < plans.size(); i++) {
        string name = plans[i][0];
        int start = toMinute(plans[i][1]);
        int playtime = stoi(plans[i][2]);

        st.push({name, playtime});

        if (i + 1 < plans.size()) {
            int nextStart = toMinute(plans[i + 1][1]);
            int available = nextStart - start;

            while (!st.empty() && available > 0) {

                if (st.top().second <= available) {
                    available -= st.top().second;

                    answer.push_back(st.top().first);
                    st.pop();
                }
                else {
                    st.top().second -= available;
                    available = 0;
                }
            }
        }
    }

    while (!st.empty()) {
        answer.push_back(st.top().first);
        st.pop();
    }

    return answer;
}