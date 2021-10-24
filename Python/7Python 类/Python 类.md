# Python类的定义

Python 类的定义模式：

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

示例：

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return f'hello {self.i}'
    
instance = MyClass()

print(instance.i)
print(instance.f())
print(type(instance))
print(isinstance(instance, MyClass))
```

运行结果：

```shell
12345
hello 12345
<class '__main__.MyClass'>
True
```



- 类里面可以定义变量，也可以叫属性（property），类成员变量；

- 类里面可以定义函数，也可以叫方法（method）。

- `instance = MyClass()` 叫类的实例化，`instance` 是类 `MyClass` 的一个实例，实例可以通过 `.` 访问属性和调用方法。有时 `instance` 也叫对象。
- `self` 是实例的别名，与其他语言里的 `this` 类似。



# 构造与析构函数

```python
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __del__(self):
        print(f'({self.x}, {self.y}) 释放了')
    
    def __str__(self):
        return f'({self.x}, {self.y})'
        
p1 = Point(1,2)
print(p1)

del p1
```

运行结果：

```python
(1, 2)
(1, 2) 释放了
```

以上结果表明，解释器在构造对象的时候会调用 `__init__()`，打印的时候会调用 `__str__()`，销毁对象的时候会调用 `__del__()`。

# 运算符重载

```python
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __del__(self):
        print(f'({self.x}, {self.y}) 释放了')
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, other):
    	return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x*other.x, self.y*other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x*other, self.y*other)
    
    def __len__(self):
        import math
        return math.sqrt(self.x**2+self.y**2)  
    
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
        
p1 = Point(1,2)
p2 = Point(2,2)

p3 = p1+p2
print(p3)
print(p1==p2)
print(p1*p2)
print(p1*2.0)
print(len(p3))
```

运行结果：

```shell
(3, 4)
False
(2, 4)
(2, 4) 释放了
(2.0, 4.0)
(2.0, 4.0) 释放了
Traceback (most recent call last):
  File "<string>", line 36, in <module>
TypeError: 'float' object cannot be interpreted as an integer
```

可见 Python 好多好用的功能就是靠这些特殊方法实现的，这些方法也叫魔法方法，类似其他语言运算符重载。

# 迭代器

```python
class Fib:
    def __init__(self, max):
        self.max = max
        self.ppre = 0 # n-2
        self.pre = 1  # n-1
        self.curr = self.pre + self.ppre # n

    def __iter__(self):
        return self

    def __next__(self):
        if self.max != 0:
            self.max -= 1
            self.curr = self.pre + self.ppre
            self.ppre = self.pre
            self.pre = self.curr
            return self.curr
        else:
            raise StopIteration


for i in Fib(5):
    print(i, end=" ")
```



# 生成器

上述代码可以简化为：

```python
class Fib:
    def __init__(self, max):
        self.max = max
        self.ppre = 0 
        self.pre = 1
        self.curr = self.pre + self.ppre

    def __iter__(self):
        while self.max != 0:
            self.max -= 1
            self.curr = self.pre + self.ppre
            self.ppre = self.pre
            self.pre = self.curr
            yield self.curr


for i in Fib(5):
    print(i, end=" ")
```

- 上述代码建议使用：[Online Python Compiler - online editor (onlinegdb.com)](https://www.onlinegdb.com/online_python_compiler) 运行，其他版本可能由于网络等原因看不到结果。
-  `yield` 关键字可以起到与 `__next()__` 类似的效果，像这种在 `__iter()__` 中使用 `yield` 关键字的迭代器又叫**生成器**。

还可以再简化一点：

```python
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
```

可以利用上述语法快速实现 `swap()`

```python
a=1
b=2
print(a, b)

a, b = b, a
print(a, b)
```



# 继承

请看如下例子：

```python
class Animal:
    common_feature = "I can move."
    
    def eat(self):
        print("I can eat.")
        
    def sleep(self):
        print("I must sleep.")
        
class Cat(Animal):
	pass

cat = Cat()
cat.eat()
cat.sleep()
print(cat.common_feature)
```
运行结果：

```shell
I can eat.
I must sleep.
I can move.
```


- 先解释一下 `pass` ：`pass` 表示一个占位符，为了语法完整，你可以去掉试试看。
- 可以看到 `Cat` 类继承了 `Animal` 类就拥有了 `Animal` 的所有属性和方法，非常适合代码复用。



再看一个例子：

```python
class Animal:
    common_feature = "I can move."
    
    def eat(self):
        print("I can eat.")
        
    def sleep(self):
        print("I must sleep.")
        
class Cat(Animal):
	
    def eat(self):
        print("除了吃，猫咪能有什么坏心思呢？")

cat = Cat()
cat.eat()
cat.sleep()
print(cat.common_feature)
```

运行结果：

```shell
除了吃，猫咪能有什么坏心思呢？
I must sleep.
I can move.
```

可以看到子类如果与父类有同样的属性或方法，优先使用子类的。

# 小结

面向对象编程挺方便的，从上述例子发现只要实现特定的方法就可以拥有某些能力，这些方法有时也称为**接口**，只要实现了接口，就可以拥有相应的功能。

面向对象编程思想还有许多好玩的，最不容错过的就是“设计模式”了。

