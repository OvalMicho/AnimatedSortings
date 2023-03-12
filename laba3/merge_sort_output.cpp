#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <chrono>
#include <vector>
#include <numeric>
#include <experimental/random>

using namespace std;

int main(){
    vector <int> a(100);
    // srand(time(NULL));
    ofstream myfile;
    myfile.open ("merge_sort_data.csv");
    for (int i=0;i<100;i++){
        a[i] = std::experimental::randint(1,100);
    }
    int i = 1;
    int j = 2;
    while (i < a.size()) {
        if (a[i - 1] < a[i]) {
            i = j;
            j = j + 1;
        }
        else {
            swap(a[i - 1], a[i]);
            for(int i=0; i<99; i++){
                    myfile << a[i] << ",";
                }
                myfile << a[99];
                myfile << std::endl;
            i = i - 1;
            if (i == 0) {
                i = j;
                j = j + 1;
            }
        }
    }
    for (int i=0;i<100;i++){
        cout << a[i] << " ";
    }
}