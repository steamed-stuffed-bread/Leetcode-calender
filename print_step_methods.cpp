int step = 4;
vector<int> path(step, 0);
int sum = 0, len = 0;

void print_res() {
    cout << "path " << sum << ": ";
    for (int i = 0; i < len; ++i) {
        cout << path[i] << ' ';
    }
    cout << endl;
}

void compute(int n) {
    if (n < 0) return;
    if (n == 0) {
        sum++;
        print_res();
        return;
    }
    for (int i = 1; i <= 2; ++i) {
        path[len] = i;
        len++;
        compute(n-i);
        len--;
    }
}

int main() {
    std::cout << "Hello World!\n";
    compute(step);
    cout << sum << " methods in total" << endl;
}
