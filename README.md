# JC-Bioinformatics 2019 Python Tutorial

此 repo 用于保存 HZAU JC-Bioinformatic 2019 暑期生物信息培训班
Python 部分所包含的文本教程、代码以及示例数据等内容。
所有内容遵循 [CC-BY-SA](https://creativecommons.org/licenses/by-sa/2.0/deed.zh) 知识共享协议。

上课采用 Jupyter notebook 讲解、运行代码。
上课的同学最好事先按照[指导材料](./doc/environment-config.md)
配置好环境 Anaconda 与 Jupyter 环境。

本教程面向的群体包括以下对Python具有不同程度了解的生物信息学相关人员：

1. 没有任何编程、计算基础的初学者。
2. 有使用其他工具栈（比如R）进行数据分析、软件开发，但对Python工具栈没有了解者。
3. 有一定编写脚本处理数据经验，希望对Python生态有更深入了解者。

## Contents

教程内容上大致分为三个部分，分在三个不同的时间段进行讲解，各个部分的内容如下：

### 一、Python 基础以及常用标准库

1. 基本成份
    + 基本对象与运算符
    + 表达式与变量
2. 如何组合
    + 内置数据结构
        - list / tuple / set / dict
    + 控制流
        - 循环 for / while
        - 分支
3. 如何抽象
    + 函数
    + 类与对象
    + 生成器
    + 选择一种编程范式
4. IO
    + 文本文件、流读写
    + 数据库读写
    + 网络 IO
5. 标准模块
    + 正则表达式
    + itertools, functools
6. 代码包装 
    + script
    + module, package
        - PyPI

### 二、Data science 相关第三方库

1. 用 Numpy 做矩阵运算
2. Pandas 处理表格数据
3. 统计与统计学习
    + Scipy
    + Statmodel
    + Scikit-Learn
4. 绘图
    + matplotlib
    + seaborn
    + 交互式图表： bokeh

### 三、命令行工具、生物信息学、计算流程

1. 命令行工具开发
    + argparse
    + click
    + Fire
2. 生物信息学常用文件格式的读写
    + Fasta, Fastq
    + BED, GFF, GTF
    + SAM, BAM
3. 计算流程开发
    + Snakemake
