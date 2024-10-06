#include <iostream>
#include <vector>

using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    int board = m * n;
    int domino = 2;
    int num;
    num = board / domino;
    cout << num;
    return 0;
}
