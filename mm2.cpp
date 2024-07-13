#include <iostream>
using namespace std;

bool prime(int num) 
{
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; i++) 
    {
        if (num % i == 0) return false;
    }
    return true;
}

int main() 
{
    int size;
    
    cout << "Enter the array size: ";
    cin >> size;

    int arr[size];
    
    cout << "Enter " << size << " elements:" << endl;
    for (int i = 0; i < size; i++) 
    {
        cin >> arr[i];
    }

    cout << "Prime numbers in the array are: ";
    for (int i = 0; i < size; i++) 
    {
        if (prime(arr[i])) 
        {
            cout << arr[i] << " ";
        }
    }
    cout << endl;

    return 0;
}
