def maybe_solution():
    pass


c = []
flag = False
n = 4
X = [[i for i in range(1, 4)] for i in range(n)]


def color(k):
    for x in X[k]:
        c.append(x)
        if maybe_solution():
            color(k+1)
        c.pop()
