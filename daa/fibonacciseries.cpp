
// print fibonacci series

// 0 1  1 2 3 5 8 13 ..............n

#include<iostream>
using namespace std;

void fibonacci_series_without_recursion(int n)
{
    int num1 = 0;
    int num2 = 1;

    for(int i = 0; i < n; i++)
    {
        cout<<num1<<" ";
        int num3 = num1 + num2;
        num2 = num1;
        num1 = num3;
    }    
}

int fibonacci_series_using_recursion(int n)
{
    if(n <= 1)
        return n;
    else
        return fibonacci_series_using_recursion(n - 1) + fibonacci_series_using_recursion(n - 2);
}

int main()
{
    int n;
    cout<<"Enter Number : "<<endl;
    cin>>n;
    cout<<"fibnacci series without recursion : "<<endl;
    fibonacci_series_without_recursion(n);

    cout<<"\nfibonacci series using recursion : "<<endl;
    for(int i = 0; i< n; i++)
    {
        cout<<fibonacci_series_using_recursion(i)<<" ";
    }
    return 0;
}