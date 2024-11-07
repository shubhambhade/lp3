#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Items {
    int value;
    int weight;
};

bool compare(Items &a, Items &b) {
    return (a.value / (double)a.weight) > (b.value / (double)b.weight);
}

double fractionalKnapsack(int w, Items *item, int n) {
    // Sort items based on the ratio: value / weight
    sort(item, item + n, compare);

    double max_val = 0;
    int cur_w = 0;

    for (int i = 0; i < n; i++) {
        // Take full weight of the item if possible
        if (cur_w + item[i].weight <= w) {
            cur_w += item[i].weight;
            max_val += item[i].value;
        } 
        else {
            // Take fraction of the item
            int rem_w = w - cur_w;
            max_val += item[i].value * (rem_w / (double)item[i].weight);
            break;
        }
    }
    return max_val;
}

int main() 
{
    int n;
    cout << "Enter item count: ";
    cin >> n;

    Items item[n];
    // Input the values
    for (int i = 0; i < n; i++) {
        cout << "Enter value of item " << i + 1 << ": ";
        cin >> item[i].value;
    }
    // Input the weights
    for (int i = 0; i < n; i++) {
        cout << "Enter weight of item " << i + 1 << ": ";
        cin >> item[i].weight;
    }

    // Enter knapsack capacity
    int w;
    cout << "Enter knapsack capacity: ";
    cin >> w;

    double result = fractionalKnapsack(w, item, n);
    cout << fixed << setprecision(1) << result << endl;

    return 0;
}
