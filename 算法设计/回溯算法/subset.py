X = [1, 2, 3]
c = []


def make_choices():
    return [True, False]


def is_final_solution(k):
    return k == len(X)


def forward(x, c, k):
    if x:
        c.append(X[k])


def rollback(x, c, k):
    if x:
        c.pop()


def subset(k):
    if is_final_solution(k):
        print(c)
        return

    for x in make_choices():
        forward(x, c, k)
        subset(k+1)
        rollback(x, c, k)


subset(0)
