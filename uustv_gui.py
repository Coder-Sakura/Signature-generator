from tkinter import *
from tkinter.ttk import Combobox
from uustv import *
class GUI(object):
	def __init__(self):
		self.window_title = '签名生成器--网络精英--2019.04.12'
		self.label_text = '输入签名字样'
		self.button_text = '点击生成'
		self.values = ['个性签','连笔签','潇洒签','草体签','合体签','商务签','可爱签']
		self.sizes = [10,20,30,40,50,60,70]

	def parts(self):		# 部件
		part = Tk()
		part.title(self.window_title)
		part.geometry('545x330')	# 窗口大小

		# 定义label,文字区域,只能看不能点,设置文字，文字字体和文字大小
		label1 = Label(part,text='设计字样',font=('华文行楷',20))
		label1.grid()	# 定义布局格式，grid()表示网格格式
		# label1.pack()	# 定义布局格式，grid()表示网格格式

		# 输入框
		enter = Entry(part,font=('微软雅黑',20))
		enter.grid(row=0,column=1)
		# enter.pack(row=0,column=1)

		# 字体样式选择
		numberChosen = Combobox(part, width=12, state='readonly')
		# numberChosen = Combobox(part, width=12, state='editable')
		numberChosen['values'] = self.values
		numberChosen.current(0)
		numberChosen.grid(row=1,column=0)

		# 字体大小选择
		sizesChosen = Combobox(part, width=12, state='readonly')
		# sizesChosen = Combobox(part, width=12, state='editable')
		sizesChosen['values'] = self.sizes
		sizesChosen.current(5)
		sizesChosen.grid(row=1,column=1)

		# 按钮
		button = Button(part,text='点击生成',font=('微软雅黑',20),command=lambda: Spider().check(part,enter,numberChosen,sizesChosen))
		button.grid(row=2,column=0)
		# button.pack(row=1,column=0)

		# image = PhotoImage(file='{}.gif'.format(word))
		# label2 = Label(part,image=image)
		# label2.bm = image
		# label2.grid(row=3,columnspan=2)

		# 添加用户点击保存按钮后才保存
		# 点击保存按钮后，command到Spider()的一个函数，下载图片
		# Spider()的一个函数获取之前存放在self中的img_html
		# 下载完成后要在GUI上显示一行红字
		part.mainloop()
gui = GUI()
gui.parts()
















































# ['jfcs.ttf','qmt.ttf','bzcs.ttf','lfc.ttf','haku.ttf','zql.ttf','yqk.ttf']
# word = input('word:')
# print('''
# jfcs.ttf ——> 个性签
# qmt.ttf ——> 连笔签
# bzcs.ttf ——> 潇洒签
# lfc.ttf ——> 草体签
# haku.ttf ——> 合体签
# zql.ttf ——> 商务签
# yqk.ttf ——> 可爱签	
# 	''')
# fonts = input('fonts:')
# Spider().post_img(word,fonts)

# image = ImageTk.PhotoImage(file=xxx.gif)


