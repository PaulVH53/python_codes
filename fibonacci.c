#include <stdio.h>

long fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        long a = 0, b = 1, temp;
        for (int i = 2; i <= n; i++) {
            temp = a;
            a = b;
            b = temp + b;
        }
        return b;
    }
}

