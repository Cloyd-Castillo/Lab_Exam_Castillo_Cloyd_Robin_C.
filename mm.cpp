#include <iostream>
using namespace std;

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

    int sum = 0;
    for (int i = 0; i < size; i++) 
    {
        if (arr[i] % 2 == 0) 
        {
            sum += arr[i];
        }
    }

    cout << "The sum of all even numbers in the array is: " << sum << endl;

    return 0;
}