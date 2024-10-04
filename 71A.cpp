#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

    int num;
    cin >> num;
    vector<string> StringRes;

    for (int i = 1; i <= num; i++) {
        string words;
        cin >> words;

        if (words.length() <= 10) {
            StringRes.push_back(words);
        }
        else {
            char first = words[0];
            char last = words[words.length() - 1];
            int middle = words.length() - 2;
            string str_middle = to_string(middle);
            string res = first + str_middle + last;
            StringRes.push_back(res);
        }
    }
    for (int i = 0; i < StringRes.size(); i++) {
        cout << StringRes[i] << endl;
    }
    return 0;
}
