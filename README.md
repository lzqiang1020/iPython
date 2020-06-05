# 前言
1. 学习并记录 python 的基本知识；  
2. 记录练习的 python 代码；
3. 版本：Py 3;
<br><br>
## 附. 代码规范
#### **1. 编码**
- 如无特殊情况, 文件一律使用 UTF-8 编码，建议文件头部加入`#-*-coding:utf-8-*-`标识编码
```python
# -*- coding:utf-8 -*-
```
注意：Py3版本后默认使用 UTF-8 编码。
<br/><br/>
#### **2. import 语句**
- import语句应该放在文件头部，置于模块说明及docstring之后，于全局变量之前；
- import 语句应该分行书写
- import语句应该使用绝对路径
- 如果发生命名冲突，则可使用命名空间
<br/><br/>
#### **3. 缩进**
- 统一使用 4 个空格进行缩进
<br/><br/>
#### **4. 行宽**
- 每行代码尽量不超过 80 个字符(在特殊情况下可以略微超过 80 ，但最长不得超过 120)  
> 理由：
> - 这在查看 side-by-side 的 diff 时很有帮助  
> - 方便在控制台下查看代码  
> - 太长可能是设计有缺陷
#### **5. 引号**
- 自然语言使用双引号 "..."  
- 机器标识符使用单引号 '...'，例如 dict 里的 key  
- 正则表达式 使用原生的双引号 r"..."  
- 文档字符串 (docstring) 使用三个双引号 """......"""
> 简单说，自然语言使用双引号，一般标识符使用单引号，因此 代码里多数应该使用单引号
#### **6. 空行**
- 模块级函数和类定义之间空两行；
- 类成员函数之间空一行；
- 可以使用多个空行分隔多组相关的函数
- 函数中可以使用空行分隔出逻辑相关的代码

#### **7. 空格**
- 在二元运算符两边各空一格[=,-,+=,==,>,in,is not, and]
- 左括号之后，右括号之前不要加多余的空格
- 字典对象的左括号之前不要多余的空格（包括索引访问）
- 不要为对齐赋值语句而使用的额外空格
- 函数的参数列表中，逗号之后要有空格
- 函数的参数列表中，默认值等号两边不要添加空格
#### **8. 换行**
- Python 支持括号内的换行。这时有两种情况  
1）第二行缩进到括号的起始处  
2）第二行缩进 4 个空格，适用于起始括号就换行的情形
```python
# 第一种情况
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 第二种情况
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
- 使用反斜杠\换行，二元运算符+ .等应出现在行末；长字符串也可以用此法换行
```python
session.query(MyTable).\
        filter_by(id=1).\
        one()
```
- 禁止复合语句，即一行中包含多个语句；
- if/for/while一定要换行：
#### **9. 文档字符串 docstring**
docstring 的规范中最其本的两点：
1. 所有的公共模块、函数、类、方法，都应该写 docstring；私有方法不一定需要，但应该在 def 后提供一个块注释来说明。
2. docstring 的结束 """ 应该独占一行，除非此 docstring 只有一行。
#### **10. 注释**
- 行注释  
至少使用两个空格和语句分开，注意不要使用无意义的注释。
- 块注释  
“#”号后空一格，段落间用空行分开（同样需要“#”号）
#### **10-1. 注释添加建议**
- 在代码的关键部分(或比较复杂的地方), 能写注释的要尽量写注释
- 比较重要的注释段, 使用多个等号隔开, 可以更加醒目, 突出重要性
```python
app = create_app(name, options)

# =====================================
# 请勿在此处添加 get post等app路由行为 !!!
# =====================================

if __name__ == '__main__':
    app.run()
```
- 不要在文档注释复制函数定义原型, 而是具体描述其具体内容, 解释具体参数和返回值等
- 文档注释不限于中英文, 但不要中英文混用
- 文档注释不是越长越好, 通常一两句话能把情况说清楚即可
- 模块、公有类、公有方法, 能写文档注释的, 应该尽量写文档注释

#### **11. 命名规范**
- 模块名  
模块使用小写命名，首字母保持小写，多个单词用下划线连接
- 类名  
类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头  
- 函数名  
    - 函数名一律小写，如有多个单词，用下划线隔开  
    - 私有函数在函数前加一个下划线_
- 变量名  
变量名尽量小写, 如有多个单词，用下划线隔开
- 常量  
常量采用全大写，如有多个单词，使用下划线隔开

--- end ---