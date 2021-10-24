#include <iostream>
#include <exception>

using namespace std;

template <typename T>
struct LinkList
{
private:
    struct Node
    {
        T data;
        Node *next;
    };

    Node *head;

public:
    LinkList()
    {
        head = nullptr;
    }

    /* insert value at index
    return index if success
    else throw out of index exception.
    */
    size_t insert(T value, size_t index = 0)
    {
        size_t i = index;
        // insert at head
        if (i == 0)
        {
            Node *tmp = new Node;
            tmp->data = value;
            tmp->next = head;
            head = tmp;
            return 0;
        }

        // insert at other place
        for (Node *p = head; p != nullptr; p = p->next)
        {
            if (i == 1)
            {
                Node *tmp = new Node;
                tmp->data = value;
                tmp->next = p->next;
                p->next = tmp;
                return index;
            }
            --i; // Do not use i=i-1;
        }

        throw range_error("Out of index.");
    }

    void show()
    {

        for (Node *p = head; p != nullptr; p = p->next)
        {
            cout << p << ": " << p->data << "|" << p->next << "  ";
        }
        cout << endl;
    }

    /* remove nth elements
     * return n if success
     * else throw out of index exception.
    */
    size_t remove(size_t index)
    {
        size_t i = index;
        Node *p = head;

        // remove first element
        if (i == 0)
        {
            head = p->next;
            delete p;
            return 0;
        }

        // remove other elements
        for (; p->next != nullptr; p = p->next)
        {
            if (i == 1)
            {
                Node *tmp = p->next;
                p->next = (p->next)->next;
                delete tmp;
                return index;
            }
            --i;
        }

        // out of index
        throw range_error("Out of index.");
    }

    T operator[](size_t index)
    {
        int i = index;
        for (Node *p = head; p != nullptr; p = p->next)
        {
            if (i == 0)
            {
                return p->data;
            }
            --i;
        }
        throw range_error("Out of index.");
    }
};

int main()
{
    LinkList<int> numbers;
    numbers.insert(5);
    numbers.insert(4);
    numbers.insert(3);
    numbers.insert(2);
    numbers.insert(1);
    numbers.insert(0, 2);
    numbers.show();
    cout << "index:2 " << numbers[2] << endl;
    return 0;
}