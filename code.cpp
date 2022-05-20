#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>

using namespace std;

vector<vector<double>> Data = {
    { 1000,   700,   500,  1100,     1,     0,     0,     0,     0,     0, 180000 },
    {   30,    20,    20,    35,     0,     1,     0,     0,     0,     0,   5000 },
    {    1,     0,     0,     0,     0,     0,     1,     0,     0,     0,    100 },
    {    0,     1,     0,     0,     0,     0,     0,     1,     0,     0,     80 },
    {    0,     0,     1,     0,     0,     0,     0,     0,     1,     0,    100 },
    {    0,     0,     0,     1,     0,     0,     0,     0,     0,     1,     60 },
    {  -70,   -80,   -60,   -80,     0,     0,     0,     0,     0,     0,      0 }
};

void printer() {
    for (auto i : Data) {
        for (auto j : i) cout << setw(7) <<  j << " ";
        cout << "\n";
    }
}

int check_min() {
    int index = -1;
    for (int i = 1; i < 11; ++i) {
        if (Data[6][i] < 0. && Data[6][i] < Data[6][index]) {
            index = i;
            // cout << Data[6][i] << " " << Data[6][index] << " \n";
            // cout << "Index: " << index << "\n";
        }
    }
    // cout << index << "\n";
    return index;
}

int check_least_in_col(int col) {
    double score = 1e9;
    int index = -1;
    for (int i = 0; i < 6; ++i) {
        if (Data[i][col] != 0) {

            double cur_score = Data[i][10] / Data[i][col];

            if (cur_score < score) {
                score = cur_score;
                index = i;
            } 
        }
    }

    return index;
}

int main() {

    int t;
    while ((t = check_min()) != -1) {
        int index = check_least_in_col(t);
        // cout << Data[index][t] << "\n";

        if (Data[index][t] != 1) {
            double div = Data[index][t];
            for (int col = 0; col < 11; ++col) {
                Data[index][col] /= div;
            }
        }

        // printer();

        for (int row = 0; row < 7; ++row) {
            if (row != index && Data[row][t] != 0) {
                double div = Data[row][t];
                for (int col = 0; col < 11; ++col) {
                    Data[row][col] -= Data[index][col] * div;
                }
            }
        }

        printer();
        // exit(0);
    }

    cout << Data[6][10];
}