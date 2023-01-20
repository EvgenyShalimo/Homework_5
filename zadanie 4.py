from datetime import datetime
import timeit


def test_1(func):
    def test_2():
        start = datetime.now()
        func()
        print(f'Скорость выполнения {str(func).split()[1]} =', datetime.now() - start)
    return test_2

@test_1
def test_2():
    x = []
    for i in range(1000000):
        if i > 0:
            x.append(i)


@test_1
def test_3():
    c = []
    for i in range(1000000000):
        if i > 0:
            c.append(i)


test_2()
test_3()
