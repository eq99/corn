X = {1, 2, 3}
c = []


def make_choices(c):
    return X-set(c)


def is_final_solution(c):
    return len(c) == len(X)


def permutation():
    if is_final_solution(c):
        print(c)
        return

    for x in make_choices(c):
        c.append(x)
        permutation()
        c.pop()


permutation()
