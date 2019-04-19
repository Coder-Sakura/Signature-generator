---

>  ## 说在前面的话
>
>  本篇概述：主要记录爬虫+GUI制作签名生成器
>
>  详细解析地址：https://coder-sakura.github.io/blog/2019/04/19/signature-generator/

---

## 1、爬虫实现

+ 暂时留空，本篇先解析代码

---

## 2、GUI实现

+ 暂时留空，本篇先解析代码

---

## 3、py说明

### 1. uustv.py ——> 爬虫模块

### 2. uustv_gui.py  ——> GUI模块

### 3. 生成软件

```python
# 1.首先安装pyinstaller
pip3 install pyinstaller

# 2.在2个py的所在目录调出cmd，输入以下命令:
pyinstaller -F -w uustv.py uustv_gui.py
# 在生成的文件夹中找到dict文件夹,其下有exe文件,便是最终的签名生成器

# 3.如果需要自定义软件图标,需要自己准备好适当尺寸的ico格式图片
# 打包的时候使用-i xxx.ico 来指定自定义的ico图标
```

