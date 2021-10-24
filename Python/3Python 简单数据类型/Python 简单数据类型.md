# 数字

Python 支持 `int, float , Complex` 等数字类型，并且可以表示成常见的进制。

以下都是合法的整数：

```python
7     2147483647                        0o177    0b100110111
3     79228162514264337593543950336     0o377    0xdeadbeef
      100_000_000_000                   0b_1110_0101
```

:bulb: `_` 用作分割符，以提高可读性。

以下是合法的浮点数：

```python
3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93
```

以下是合法的复数：

```python
3.14j   10.j    10j     .001j   1e100j   3.14e-10j   3.14_15_93j
```

# 字符串

## Python 如何表示字符串？

字符串是一系列的字符序列，Python中用单引号('')，双引号("")，或者三个单引号(''' ''')三个双引号(""" """)来表示字符串常量。Python 不像 C 语言那样区分字符与字符串。

一般三引号字符串常用作文档注释。例如：

```python
def sayHi():
    '''
    I am a say hi function.
    '''
    print('hi')
```

有些编辑器当你把鼠标放在函数名字上的时候可以看到这段文档，是不是很方便呢？

## Python 如何表示特殊字符？

Python 用转义的方法表示特殊字符，常见转义字符表示：  

| 转义序列 | 意义                               |
| -------- | ---------------------------------- |
| `\`      | 转义符                             |
| `\’`     | 单引号（’）                        |
| `\"`     | 双引号（”）                        |
| `\n`     | ASCII 换行符（LF）                 |
| `\r`     | ASCII 回车符（CR）                 |
| `\t`     | ASCII 水平制表符（TAB）            |
| `\ooo`   | 三个八进制数为一组表示一个特殊字符 |
| `\xhh`   | 两个八进制数为一组表示一个特殊字符 |

Unicode 字符表示规则如下：

| 转义序列   | 意   义                                  |
| ---------- | ---------------------------------------- |
| \N{name}   | Unicode 数据库中以 name 命名的字符       |
| \uxxxx     | 4个16进制字符为一组表示一个 Unicode 字符 |
| \Uxxxxxxxx | 8个16进制字符为一组表示一个 Unicode 字符 |

示例：

```python
print('\666')
print('\x6f')
print("\N{GREEK SMALL LETTER BETA}")
print("\N{BLACK SPADE SUIT}")
print('\u73de')
print('\U0001F440')
print('\U0001F4AF')
# ƶ
# o
# β
# ♠
# 珞
# 👀
# 💯
```

## 什么是 raw string?

Raw string 以`r` 开头，转义符无效，当做普通的 `\\`。

示例1：

```python
looke = 'Looke\nLooke.com'
raw_looke = r'Looke\nLooke.com'
print(looke)
print('----------------')
print(raw_looke)

path= r'C:\Users\Looke\Desktop\python'
print(path)
```

示例二：

```python
import re


html='''
<div class="star">
  <span class="rating5-t"></span>
  <span class="rating_num" property="v:average">9.7</span>
  <span property="v:best" content="10.0"></span>
  <span>2386600人评价</span>
</div>
'''
rate_regex = '<span class="rating_num" property="v:average">(\d+\.\d+)</span>'
rate = re.findall(rate_regex, html)
print(rate)
# ['9.7']
```

以上两个例子说明 raw 字符串用于表示路径与正则表达式时非常方便。

## 什么是字节文本？

字节文本总是以 'b' 或 'B' 开头；它们会生成 [bytes](https://docs.python.org/3/library/functions.html#bytes) 类型实例而不是 [str](https://docs.python.org/3/library/stdtypes.html#str) 类型。它们可能只包含 ASCII 字符；大于或等于 128 的数字必须使用转义字符表示。

示例：

```python
one_str = "少壮不努力，老大学Python"
str_to_byte = one_str.encode('utf-8')
print(str_to_byte)
#b'\xe5\xb0\x91\xe5\xa3\xae\xe4\xb8\x8d\xe5\x8a\xaa\xe5\x8a\x9b\xef\xbc\x8c\xe8\x80\x81\xe5\xa4\xa7\xe5\xad\xa6Python'

byte_to_str = str_to_byte.decode('utf-8')
print(byte_to_str)
#少壮不努力，老大学Python
```



## 为什么要用字节文本？

文本在内存中以对象存在，可以有复杂的结构，但是文件格式保存或进行网络传输的时候以字节序列的方式存在。



## 什么是格式字符串？

格式字符串能在字符串中方便的嵌入变量值，书写格式为：以 `f` 开头，变量用`{}`界定，还可以在 `{}` 用 `:` 控制格式。

示例：

```python
name = 'LookeLooke.com'
print(f'Hello {name}')

x = 9
print(f'{x} * {x} = {x*x:.2f}')
```

## 字符串的运算

假设有字符串`str1 = 'Hello ',str2 = 'LookeLooke'`

| 操作符 | 描述                                               | 实例                             |
| :----- | :------------------------------------------------- | :------------------------------- |
| +      | 字符串连接                                         | `str1 + str2 # Hello LookeLooke` |
| *      | 重复输出字符串                                     | `str1 * 2 # Hello Hello `        |
| []     | 通过索引获取字符串中字符                           | `str1[1] # e`                    |
| [ : ]  | 截取字符串(切片，slice)                            | `str2[2:4] # ok`                 |
| in     | 成员运算符 - 如果字符串中包含给定的字符返回 True   | `'ok' in str2 # True`            |
| not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True | `'o' not in str1 # False`        |

## 常见的字符串函数

| 方法           | 解释                                                         |
| :------------- | :----------------------------------------------------------- |
| `len(string)`  | 返回字符串长度                                               |
| `lower()`      | 全部转为小写                                                 |
| `upper()`      | 全部转为大写                                                 |
| `capitalize()` | 将字符串的第一个字符转换为大写                               |
| `find(str)`    | 查找子字符串 `str`                                           |
| `isalnum()`    | 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False |
| `isdigit()`    | 如果字符串只包含数字则返回 True 否则返回 False.              |
| `join()`       | 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
| `lstrip()`     | 截掉字符串开头的空格或指定字符                               |
| `rstrip()`     | 截掉字符串结尾的空格或指定字符                               |
| `strip()`      | 截掉字符串两头的空格或指定字符                               |
| `split()`      | 分割字符串                                                   |

示例：

```python
name = "LookeLooke.com"

print(f'len: {len(name)}')
print(name.lower())
print(name.upper())
print(name.capitalize())
print(f'find: {name.find("ok")}')
print(name.isdigit())
print(' '.join(["Hello", name]))
print("   " + name)
print(name.strip())
print(name.split('.'))
```

更多操作请搜索：Python 字符串操作，Python 字符串方法，Python string method......

