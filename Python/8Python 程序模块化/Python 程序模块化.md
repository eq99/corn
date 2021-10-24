# 什么是模块化

“维护性好，扩展性好”是软件开发的重要主题。真实的项目不像我们之前学习语言特性那样随便写几行代码，然后 `print()` 一下结果，真实的软件开发需要懂编程语言的语法，更需要懂软件背后的原理，更需要了解需求。为了控制软件开发的复杂度，需要建立不同层次的**抽象**，或者说把程序**模块化**。

 事实上，你已经学习了两个模块化的重要方法：函数与类。把零散的过程封装为函数，把零散的对象封装为类，能使你的程序简洁明了。



# 模块

函数与类的模块化只体现在一个源文件中，接下来介绍源文件之间的模块化。

1）新建一个文件夹 `Demo`，用 VS Code 打开，建立如下所以的子文件夹与文件：

![Python模块化文件夹结构](https://sophia-1303119720.cos.ap-nanjing.myqcloud.com/Python%E6%A8%A1%E5%9D%97%E5%8C%96%E6%96%87%E4%BB%B6%E5%A4%B9%E7%BB%93%E6%9E%84.png)

这里你会发现 `math_lib` 与 `Science` 文件夹下都有一个 `__init__.py` 的文件，这个文件会告诉 Python `math_lib` 与 `Science` 是一个模块。

2）向 `math_lib/add.py` 中加入如下内容：

```python
def add(x, y):
    '''
    add function
    '''
    return x + y
```

向 `math_lib/constant.py` 加入如下内容：

```python
'''
This file defines many math constants
'''
pi = 3.1415926

e = 2.718281828
```

向  `main.py` 中加入如下内容：

```python
from math_lib.add import add

print(add(3, 4))
```

3）用 `Ctrl` 加 `Tab` 上面那个符号打开终端，输入 `python main.py` 运行代码：

![Python模块化示例1](https://sophia-1303119720.cos.ap-nanjing.myqcloud.com/Python%E6%A8%A1%E5%9D%97%E5%8C%96%E7%A4%BA%E4%BE%8B1.png)

通过 `from math_lib.add import add` 引入 `math_lib` 中定义的  `add()` 就可以在 `main.py` 中使用了。



# 更多示例

`geometry/cicle.py` 如何引用 `math_lib` 定义的函数与常量呢？

1）在 `geometry/cicle.py` 中输入：

```python
'''
This file defines Circle
'''

from math_lib.constant import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return pi*self.radius**
```

2）在 `geometry/rectangle.py` 中输入：

```python
'''
This file defines Rectangle
'''
from math_lib.add import add


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_lenth(self):
        return 2*add(self.height, self.width)
```



3）重写 `main.py` :

```python
from geometry.circle import Circle
from geometry.rectangle import Rectangle

c = Circle(2)
r = Rectangle(2, 3)

print(c.get_area())
print(r.get_lenth())
```

 运行程序，得到：

![Python模块化示例2](https://sophia-1303119720.cos.ap-nanjing.myqcloud.com/Python%E6%A8%A1%E5%9D%97%E5%8C%96%E7%A4%BA%E4%BE%8B2.png)

这就是 Python 文件间模块化的示例了，是不是很简单呢？

:question: 如果在 `geometry/circle.py` 中使用：

```
from ..constant import pi
```

会发生什么？

# PyPi

[PyPI · The Python Package Index](https://pypi.org/) 是一个 Python 在线包管理器，你可以在上面找到满足你需要的包 （Package）通过 `pip` 等包管理器或者一些项目管理工具可以安装包。

安装包示例：

```shell
pip install pandas
```

以上命令安装了数据分析库 `pandas` ，查看你安装了哪些库：

```shell
pip list
```



# 虚拟环境

Python应用程序通常会使用不在标准库内的软件包和模块。应用程序有时需要特定版本的库，因为应用程序可能需要修复特定的错误，或者可以使用库的过时版本的接口编写应用程序。

这意味着一个Python安装可能无法满足每个应用程序的要求。如果应用程序A需要特定模块的1.0版本但应用程序B需要2.0版本，则需求存在冲突，安装版本1.0或2.0将导致某一个应用程序无法运行。

这个问题的解决方案是创建一个 虚拟环境。

创建一个名为 `` 的虚拟环境：

```shell
python -m venv tutorial-env
```

如果你用的 Windows，激活虚拟环境如下：

```shell
tutorial-env\Scripts\activate
```

在Unix或MacOS上，激活如下：

```shell
source tutorial-env/bin/activate
```

激活成功后你的命令提示符会多出一个：

```shell
(tutorial-env)
```

更多用法请阅读：[12. 虚拟环境和包 — Python 3.9.7 文档](https://docs.python.org/zh-cn/3/tutorial/venv.html)



# 项目管理器

目前比较好用的项目管理有：

- [pdm-project/pdm: A modern Python package manager with PEP 582 support. (github.com)](https://github.com/pdm-project/pdm)

- [python-poetry/poetry: Python dependency management and packaging made easy. (github.com)](https://github.com/python-poetry/poetry)

你可以自己安装尝试一下。
