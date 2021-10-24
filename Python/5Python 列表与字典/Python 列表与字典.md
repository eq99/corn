# 列表 List

## 什么是列表？

直接定义列表有些困难，可以通过观察例子对列表建立感性的认识。

```python
numbers = [1, 2, 3, 4]
pets = ['二哈','猫咪','仓老鼠']
empty = []
```

从上面的例子说明列表是由 `[]` 括起来的一组对象，对象之间用 `,` 隔开。

## 如何创建列表？

1）枚举列表中的元素：

```python
computer_basics = ['数学','编程设计','计算机组成原理','算法与数据结构','操作系统','计算机网络','编译原理','数据库']

print(computer_basics)
```

2）通过向空列表中添加元素:

```python
even_numbers = []
for k in range(0,5):
  even_numbers.append(2*k)

print(even_numbers)
# [0, 2, 4, 6, 8]
```

3）通过列表推导式：

```python
odds = [2*k+1 for k in range(5)]
print(odds)
# [1, 3, 5, 7, 9]

points = [(x,y) for x in range(3) for y in range(2,4)]
print(points)
# [(0, 2), (0, 3), (1, 2), (1, 3), (2, 2), (2, 3)]

evens = [x for x in range(10) if x % 2 ==0]
print(evens)
# [0, 2, 4, 6, 8]
```

4）列表的元素类型不一定相同

```python
infos = ["Looke", [2021, 8, 13], ("湖北", "武汉"), 1.0]
print(infos)
# ['Looke', [2021, 8, 13], ('湖北', '武汉'), 1.0]
```



## 如何访问列表中的元素？

1）通过下标访问

```python
program_languages = ['Python', 'C++', 'Java', 'golang', 'javascript', 'SQL', 'Rust']

print(f'学习 {program_languages[0]} 的人超帅!')
```

2）通过`for...in...`访问

```python
players = ['贝利', '马拉多纳', 'C罗', '梅西']

for player in players:
  print(player)
```



## 如何获取列表中部分元素？

通过切片的方式，切片的模式为`[i:j:k]`，其中`i`为起始下标，如果省略，则为0；`j`为结束下标，如果省略，最为最后一个元素；`k`为步长，如果省略，则为1。如果`i,j`为负数，代表从最后一个元素向前数。

请看示例：

```python
pi = [3,1,4,1,5,9,2,6]

y1 = pi[1:3]
print(y1)
# [1,4]

y2 = pi[1:8:2]
print(y2)
# [1, 1, 9, 6]

y3 = pi[1:]
print(y3)
# [1,4,1,5,9,2,6]

y4 = pi[1:-2]
print(y4)
# [1, 4, 1, 5, 9]

y5 = pi[-2:-1]
print(y5)
# [2]
```

:bulb: `[i,j]` 表示的区间是左闭右开 $[i,j)$



## 如何合并两个列表？

你可以迭代两个列表的元素把它加入到新的列表里面，不过还有如下方法：

1）加法

```python
evens = [0,2,4,8,10]
odds = [1,3,5,7,9]
numbers = evens + odds
print(numbers)
# [0, 2, 4, 8, 10, 1, 3, 5, 7, 9]
```

2）序列解包

```python
evens = [0,2,4,8,10]
odds = [1,3,5,7,9]
numbers = [*evens, *odds]
print(numbers)
# [0, 2, 4, 8, 10, 1, 3, 5, 7, 9]
```

3）`extend()`

```python
evens = [0,2,4,8,10]
odds = [1,3,5,7,9]
evens.extend(odds)
print(evens)
# [0, 2, 4, 8, 10, 1, 3, 5, 7, 9]
```



## 常用函数

| 函数       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| `append()` | 在列表末尾添加新的对象                                       |
| `count()`  | 统计某个元素在列表中出现的次数                               |
| `insert()` | 将对象插入列表                                               |
| `pop()`    | 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| `remove()` | 移除列表中某个值的第一个匹配项                               |
| `sort()`   | 对原列表进行排序                                             |
| `clear()`  | 清空列表                                                     |
| `len()`    | 求数组元素个数                                               |
| `min()`    | 求最小值                                                     |
| `max()`    | 求最大值                                                     |
| `sum()`    | 求和                                                         |

示例程序：

```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
# 2

fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

print(len(fruits))
# 7

print(fruits.pop())
print(len(fruits))
# pear
# 6

from random import randint
numbers = [randint(1, 20) for i in range(6)]
print(numbers)
print(f'min: {min(numbers)}, max: {max(numbers)}, sum: {sum(numbers)}')
# [14, 7, 16, 6, 14, 9]
# min: 6, max: 16, sum: 66
```

更多用法请阅读：

- [5. 数据结构 — Python 3.9.7 文档](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)

- [内置类型 — Python 3.9.7 文档](https://docs.python.org/zh-cn/3/library/stdtypes.html#sequence-types-list-tuple-range)

# 字典

## 什么是字典？

先看两个字典的例子：

```python
user = {
  'name': 'Looke', 
  'birthday': '2021-07-02',
  'hobby': '打豆豆'
}

print(user)

computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer)
```

从上面的例子可以看出字典是用 `{}` 括起来的键值对 (key-value)。键值对之间用 `,` 分隔。同时可以看出字典可以清楚的描述对象的属性。

## 如何建立字典？

1）像前一个例子那样的枚举法。

2）向空字典中添加条目：

```python
menu = {}
menu['广东烧鹅'] = '￥99.8'

print(menu)
# {'广东烧鹅': '￥99.8'}
```

想用 `append()` ？不好意思，对字典使用会报错：  `AttributeError: 'dict' object has no attribute 'append'` 。

## 如何访问字典中的元素？

1）通过键 (key) 访问值 (value)

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer['显卡'])
# RTX 3070TI 星耀
```

如果访问不存在的键：

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer['散热'])
# Traceback (most recent call last):
#   File "script.py", line 11, in 
#     print(computer['散热'])
# KeyError: '散热'
```

2）通过 `get()` 方法

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

print(computer.get('显卡'))
print(computer.get('散热'))
# RTX 3070TI 星耀
# None
```

你发现这两种方法的区别了吗？

3）通过 `for...in...` 方法

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

for item in computer:
  print(item, computer[item])
  
# cpu R5 5600X 散片
# 主板 微星B550M迫击炮
# 显卡 RTX 3070TI 星耀
# 内存 英睿达3200Hz 8G*2
# 硬盘 西数sn750 1T
# 电源 安钛克HCG750
# 机箱 DF700Flux
```

另外一种访问键值对的方法：

```python
computer = {
  'cpu': 'R5 5600X 散片',
  '主板': '微星B550M迫击炮',
  '显卡': 'RTX 3070TI 星耀',
  '内存': '英睿达3200Hz 8G*2',
  '硬盘': '西数sn750 1T',
  '电源': '安钛克HCG750',
  '机箱': 'DF700Flux'
}

for key, value in computer.items():
  print(key, value)
  
# cpu R5 5600X 散片
# 主板 微星B550M迫击炮
# 显卡 RTX 3070TI 星耀
# 内存 英睿达3200Hz 8G*2
# 硬盘 西数sn750 1T
# 电源 安钛克HCG750
# 机箱 DF700Flux
```

## 怎么合并两个字典？

```python
database = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': '123456',
    'HOST': 'localhost',
    'PORT': '5432'
}

redis = {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/1",
}

config = {**database, **redis}

print(config)
# {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'postgres', 'USER': 'postgres', 'PASSWORD': '123456', 'HOST': 'localhost', 'PORT': '5432', 'BACKEND': 'django_redis.cache.RedisCache', 'LOCATION': 'redis://127.0.0.1:6379/1'}

```



# 总结

列表与字典是 Python 最常见的两种容器对象，Python 还有元组 （tuple），集合 (set) 等容器，更多知识可以阅读：[5. 数据结构 — Python 3.9.7 文档](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)

