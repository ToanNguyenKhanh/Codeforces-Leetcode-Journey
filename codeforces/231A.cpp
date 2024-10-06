#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int num;
    cin >> num;
    int count = 0;
    for (int i = 1; i <= num; i++) {
        int one = 0;
        for (int j = 1; j <= 3; j++) {
            int sure;
            cin >> sure;
            if (sure == 1) {
                one += 1;
            }
        }
        if (one >= 2) {
            count += 1;
        }
    }
    cout << count;

    return 0;
}
