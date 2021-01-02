void addtobottom(stack<int>& st, int t){
    if (st.empty()) st.push(t);
    else {
        int top = st.top();
        st.pop();
        addtobottom(st, t);
        st.push(top);
    }
}

void rev(stack<int>& st) {
    if (st.empty()) return;
    int t = st.top();
    st.pop();
    rev(st);
    addtobottom(st, t);
}

int main() {
    std::cout << "Hello World!\n";
    stack<int> st;
    for (int i = 1; i <= 5; ++i) st.push(i);
    rev(st);
    while (!st.empty()) {cout << st.top() << endl; st.pop();}
}
