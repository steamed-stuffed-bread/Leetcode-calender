int divide(int num, int factor) {
    while (factor < num && (num%factor != 0)) {
        factor++;
    }
    cout << factor << endl;
    num = num/factor;
    if (factor >= num) return factor;
    return divide(num, factor);
}

int main() {
    std::cout << "Hello World!\n";
    divide(435234, 2);
}
