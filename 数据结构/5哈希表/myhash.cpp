#include <iostream>
#include <tr1/functional> /* tr1::hash */
#include <random>
#include <list>

using namespace std;

template <typename T>
struct Hash
{
private:
    size_t capacity;

    list<T> *table;

public:
    Hash(size_t c)
    {
        capacity = c;
        table = new list<T>[capacity];
    }

    size_t hash_function(T key)
    {
        return tr1::hash<T>()(key) % capacity;
    }

    void insert_element(T key)
    {
        size_t index = hash_function(key);
        table[index].push_back(key);
    }

    void delete_element(T key)
    {
        size_t index = hash_function(key);
        for (auto it = table[index].begin(); it != table[index].end(); ++it)
        {
            if (*it == key)
            {
                table[index].erase(it);
                break;
            }
        }
    }

    void show()
    {
        for (int i = 0; i < capacity; ++i)
        {
            cout << i;
            for (auto x : table[i])
                cout << "--->" << x;
            cout << endl;
        }
    }
};

int main()
{
    Hash<int> h(7);

    // set random engine
    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution<size_t> dist(10, 100);

    for (int i = 0; i < 10; ++i)
        h.insert_element(dist(mt));

    h.show();
}