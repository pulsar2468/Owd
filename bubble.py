import random


def bubble():
    n = len(a)

    while True:
        k = 0;
        for i in range(0, n - 1):

            if a[i] > a[i + 1]:
                aus = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aus
                k = 1
        if k == 0:
            break;

        --n;


a = [random.randint(0, 10) for i in range(1, 10)]
print(a)
bubble()
print(a)
