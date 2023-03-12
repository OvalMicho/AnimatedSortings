#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <chrono>
#include <vector>
#include <numeric>

using namespace std;
int main(){
    vector <int> values(100);
    srand(time(NULL));
    ofstream myfile;
    myfile.open ("shell_sort_data.csv");
    for (int i=0;i<100;i++){
        values[i] = rand()%100 + 1;
    }
    int N =100;
	for (int s = N / 2; s > 0; s /= 2) {
		for (int i = s; i < N; ++i) {
			for (int j = i - s; j >= 0 && values[j] > values[j + s]; j -= s) {
				int temp = values[j];
				values[j] = values[j + s];
				values[j + s] = temp;
                for(int i=0; i<99; i++){
                    myfile << values[i] << ",";
                }
                myfile << values[99];
                myfile << std::endl;
			}
		}
	}
    for (int i=0;i<100;i++){
        cout << values[i] << " ";
    }
}