#include <iostream>

using namespace std;

template <typename T>
void displayArrayAddress(T a[], size_t n, size_t m)
{
    for (int i = 0; i < n; ++i)
    {
        cout << a + i << ": " << *(a + i) << endl;
        for (int j = 0; j < m; ++j)
        {
            cout << "    " << *(a + i) + j << ": " << *(*(a + i) + j) << endl;
        }
    }
}

int main()
{
    int numbers[3][2] = {{1, 2}, {3, 4}, {5, 6}};
    displayArrayAddress(numbers, 3, 2);
    return 0;
}