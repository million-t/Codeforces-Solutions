#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        priority_queue<pair<int, int>> heap;
        for (int i = 0; i < n; i++) {
            heap.push({-a[i], i});
        }

        vector<int> ans;
        while (!heap.empty()) {
            auto [cur, ind] = heap.top();
            heap.pop();

            if (-cur > k) {
                heap.push({cur + k, ind});
            } else {
                ans.push_back(ind + 1);
            }
        }

        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
    }

    return 0;
}