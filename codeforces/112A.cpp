#include <iostream>
#include <string>
#include <algorithm> 
using namespace std;
 
int main() {
    string str1, str2;
    cin >> str1;
    cin >> str2;
 
    transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
    transform(str2.begin(), str2.end(), str2.begin(), ::tolower);
 
    int n = min(str1.length(), str2.length());
    for (int i = 0; i < n; i++) {
        char chr1 = str1[i];
        char chr2 = str2[i];
        int asciiValue1 = static_cast<int>(chr1);
        int asciiValue2 = static_cast<int>(chr2);
 
        if (asciiValue1 < asciiValue2) {
            cout << -1 << endl;  
            return 0;
        }
        else if (asciiValue1 > asciiValue2) {
            cout << 1 << endl;  
            return 0;
        }
    }
 
    if (str1.length() < str2.length()) {
        cout << -1 << endl;  
    }
    else if (str1.length() > str2.length()) {
        cout << 1 << endl;  
    }
    else {
        cout << 0 << endl;  
    }
 
    return 0;
}
