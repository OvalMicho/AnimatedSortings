#!/bin/bash
echo compiling
g++ shell_sort_output.cpp -o shell
g++ merge_sort_output.cpp -o merge
g++ quicksort_output.cpp -o quick
echo running
./shell
./merge
./quick
python3 shell.py
python3 merge.py
python3 quick.py
#echo imdone
