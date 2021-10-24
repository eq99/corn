'''
class Fib:
    def __init__(self, max):
        self.max = max
        self.pre = 1
        self.ppre = 1

    def __iter__(self):
        self.curr = 1
        return self

    def __next__(self):
        if self.max != 0:
            self.max -= 1
            result = self.pre + self.ppre
            self.ppre = self.pre
            self.pre = self.curr
            self.curr = result
            return result


for i in Fib(5):
    print(i)

'''


class Fib:
    def __init__(self, max):
        self.max = max
        self.pre = 0
        self.curr = 1

    def __iter__(self):
        while self.max != 0:
            self.max -= 1
            self.pre, self.curr = self.curr, self.curr+self.pre
            yield self.curr


for i in Fib(5):
    print(i, end=" ")
