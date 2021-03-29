#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;

class LRU{
public:
    LRU(int c):capacity(c){};
    string get(string key) {
        if (!m.count(key)) return "";
        l.splice(l.begin(), l, m[key]);
        m[key] = l.begin();
        return m[key]->val;
    }
    
    void put(string key, string val) {
        if (!m.count(key)) {
            if (m.size() == capacity) {
                m.erase(l.back().key);
                l.pop_back();
            }
        }
        l.push_front(Node(key, val));
        m[key] = l.begin();
    }
private:
    struct Node {
        string key;
        string val;
        Node(string k, string v):key(k), val(v){};
    };
    int capacity;
    list<Node> l;
    unordered_map<string, list<Node>::iterator> m;
};

int main() {
    LRU l(2);
    l.put("abc", "def");
    cout << l.get("abc") << endl;
    std::cout << "Hello World!\n";
}
