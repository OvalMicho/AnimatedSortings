#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <ctime>
#include <cstdlib>


using namespace std;

struct IntRange
{
    int *begin;
    int *end;
};

void swap(int *x,int* y){
    int a = *x;
    *x = *y;
    *y = a;
}

template<typename Predicate>
int *partition(IntRange range, Predicate p, ofstream &file, IntRange o){
    int *l = range.begin;
    int *h = range.end - 1;
    //int n= range.end - range.begin;
    while (true){
        while(l<range.end && p(*l) == true){
            l++;
        }
        while(h>range.begin && p(*h) == false){
            h--;
        }
        if(h>l){
            swap(l,h);
            for(int i=0; i<99; i++){
                file << o.begin[i] << ",";
            }
            file << o.begin[99];
            file << std::endl;
        }
        else{
            return l;
        }
    }
}

void quicksort(IntRange range,ofstream &file, IntRange o){
    if (range.begin == range.end){return;}
    int y = range.begin[0];
    auto middle1 = partition(range,[y](int x){return x < y;}, file, o);
    // IntRange r = {middle1,range.end};
    auto middle2 = partition({middle1,range.end},[y](int x){return x == y;}, file, o);
    quicksort({range.begin,middle1}, file, o);
    quicksort({middle2,range.end}, file, o);
}

// void quickselect(IntRange range,int *ptr){
//     if (range.begin == range.end){return;}
//     int y = range.begin[0];
//     auto middle1 = partition(range,[y](int x){return x < y;});
//     // IntRange r = {middle1,range.end};
//     auto middle2 = partition({middle1,range.end},[y](int x){return x == y;});
//     if(ptr>=middle2){
//         quickselect ({middle2,range.end},ptr);
//     }
//     else{
//         if(ptr>middle1 and ptr<middle2){
//             return;
//         }
//         else{
//             quickselect ({range.begin,middle1},ptr);
//         }
//     }
    
// }

int main(){
    // int 100;
    // cin >> n;
    int m[100];
    // srand(time(NULL));
    ofstream myfile;
    myfile.open ("quicksort_data.csv");
    for (int i=0;i<100;i++){
        m[i] = rand() % 100 + 1;
    }
    IntRange r = {&m[0],&m[0] + 100};
    IntRange o = r;
    int *p = &m[4];
    ofstream &da = myfile;
    quicksort(r, da, o);
    for (auto now : m){
        cout << now << ",";
    }
    myfile.close();
}