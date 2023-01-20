slova = ('ага', 'течет', 'летел', 'привет', 'пока')


def pol(x):
    if x == x[::-1]:
        return x


slova_1 = list(filter(pol, slova))
print(slova_1)
