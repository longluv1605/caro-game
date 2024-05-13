#include <bits/stdc++.h>

using namespace std;

int countNew(int K, int old[], int next[]) {
    int count = 0;
    int oldPointer = 0, nextPointer = 0;
    while (oldPointer < K && nextPointer < K) {
        if (old[oldPointer] == next[nextPointer]) {
            nextPointer++;
        }
        else if (old[oldPointer] < next[nextPointer]) {
            oldPointer++;
        }
        else {
            count++;
            nextPointer++;
        }
    }

    return count + K - nextPointer;
}

int main() {
    int K = 3;
    int old[] = {1, 3, 4};
    int next[] = {1, 3, 5};

    cout << countNew(K, old, next) << endl;
    return 0;
}