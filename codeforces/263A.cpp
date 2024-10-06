#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int matrix[5][5];  
    int x, y;         

    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            cin >> matrix[i][j];
            if (matrix[i][j] == 1) {
                x = i + 1;  
                y = j + 1;  
            }
        }
    }

    int steps = abs(x - 3) + abs(y - 3);
    cout << steps << endl;

    return 0;
}
