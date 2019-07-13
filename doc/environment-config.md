# 环境配置

+ [Anaconda](#Anaconda)
+ [Jupyter](#Jupyter)

## Anaconda

Anaconda 提供了一个跨平台的 Python 发行版以及
通用的软件、软件包依赖管理系统，非常适合于生物信息软件的管理。
本文提供一系列关于如何配置基于 Anaconda 的 Python 计算环境配置指导。

### 下载

Anaconda 是一个较为完整庞大的 Python 发行版，内置一系列常用的 Python 包以及
开发工具，安装包比较大。通常我们推荐安装 Anaconda 的精简版本 Miniconda，
它仅提供了 Anaconda 套件中最为核心的部分，
包括一个 Python 解释器，一个软件管理器: conda，以及一些其它的必要设施。
安装它只需要打开官网
[下载页面](https://docs.conda.io/en/latest/miniconda.html)
选择与操作系统相对应的版本进行下载。

注意：这里最好不要下载 Python 2 的版本
（2020年Python社区就会放弃对于Python2的支持，
很多[第三方库](https://python3statement.org/)也会这么做，
而现在已经是 9102 年了..），虽然你可以使用conda创建任意版本的
Python 环境，但你的 base 会默认是 Python2（虽然你可以随时改掉它），
Python2 的时代已经过去了，让它走吧。

### 安装

下载完成后，根据不同操作系统对应版本的不同进行安装，Windows 下
只需按照 exe installer 的指导一步步安装即可。Linux, Mac
下需要执行安装脚本进行安装。

``` bash
bash Miniconda3-latest-Linux-x86_64.sh
```

详细的操作可以参考[此处](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

### 配置

安装后为保证 conda 能被操作系统找到，需要正确配置。Windows 下
需要将 miniconda 的 bin 路径（位于miniconda的安装目录下）
放在 PATH 环境变量下。
关于如何修改 PATH 变量，可以参考[这里](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)。

Linux 下，安装后需要确保 conda 被正常配置，可执行 conda init 指令完成配置。

``` bash
/path/to/miniconda/bin/conda init
```

注意，此处 `/path/to/miniconda` 代表的是你的miniconda的安装路径。
完成初始化后，conda 会修改你的 bashrc 文件，需要使用 source 命令对其重新加载：

``` bash
source ~/.bashrc
```

### 使用虚拟环境管理软件

在实际使用情景下，有时软件包之间会存在[依赖关系冲突](https://en.wikipedia.org/wiki/Dependency_hell)，
conda 提供了一种解决方案，创建不同的虚拟环境将彼此分割开来，
从而解决依赖冲突问题。日常使用时为不同任务创建不同的虚拟环境是一种好习惯。

#### 创建虚拟环境

创建一个为本课程使用的环境，命名为 jcbio：

``` bash
conda create -n jcbio python=3.6  # 创建虚拟环境 jcbio，指定 Python 版本为 3.6
```

#### 切换至虚拟环境

我们可以列出当前所有的虚拟环境：

``` bash
conda env list
```

切换至课程所使用的虚拟环境 jcbio：

``` bash
conda activate jcbio
```

#### 安装软件、软件包

在该虚拟环境中，安装上课所需的软件包：

``` bash
conda install numpy scipy matplotlib jupyter
```

## Jupyter

![](https://jupyter.org/assets/jupyterpreview.png)

[Project Jupyter](https://jupyter.org/) 
为 Python 以及其他众多编程语言提供了十分便利的
交互式计算环境： Jupyter notebook 与 Jupyter Lab。
前者 Jupyter notebook 顾名思义，你可以理解为就是一个记事本，我们可以在记事本中写入很多各种各样的 内容，比如文字、图片、视频等等，你可以用它来写日记、作实验记录，甚至用来写书。
和一般所理解的 notebook 没有什么不同。<del>真的吗？</del>
只不过比较特殊的是它可以嵌入代码，并且可以实时的运行代码，并返回运行的结果。
这样就很适合我们来用它作交互式的数据分析了，并且甚至分析完当场就有了一份
实验记录加数据分析报告。多好用啊！这也是我们的教程选择它的原因。
至于 Jupyter Lab，你可以理解为是 notebook 的加强版，有更多的功能，
但也更加复杂，我们这里只介绍 notebook。

这里我们介绍一些 Jupyter notebook 的基本使用。
在上一步中，我们已经完成了 Jupyter 环境的安装，可以打开终端，输入：

``` bash
jupyter notebook
```

启动一个 Jupyter server，如果你在安装了图形界面的操作系统中进行操作，
这时会自动弹出一个浏览器窗口
