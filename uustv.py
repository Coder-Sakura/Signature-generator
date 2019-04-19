import requests
import time
from bs4 import BeautifulSoup
# pip3 install beautifulsoup4
# pip3 install requests
from tkinter import messagebox
from tkinter import *	# PhotoImage
class Spider(object):
	def __init__(self):
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
	}
		self.url = 'http://m.uustv.com/'
		self.values = ['个性签','连笔签','潇洒签','草体签','合体签','商务签','可爱签']
		self.font = ['jfcs.ttf','qmt.ttf','bzcs.ttf','lfc.ttf','haku.ttf','zql.ttf','yqk.ttf']
		self.v_f = dict(zip(self.values,self.font))
		self.word = ''
		self.fonts = ''
		self.size = 60

	def check(self,part,enter,numberChosen,sizesChosen):
		self.part = part
		self.word = enter.get()
		self.fonts = numberChosen.get()		# 文字
		self.size = sizesChosen.get()
		if not enter.get():
			messagebox.showinfo('提示','请输入需要生成签名的文字')
		else:
			if self.fonts in self.v_f:
				self.fonts = self.v_f[self.fonts]	# 文字转换成字体格式名称
				# messagebox.showinfo('提示',word)
				# messagebox.showinfo('提示',fonts)
				self.post_img()

	def post_img(self):		# 发送请求并获取图片地址及二进制内容
		data = {
			'word': self.word,
			# 'sizes': '60',
			'sizes': self.size,
			'fonts': self.fonts,
			# 'fonts': 'jfcs.ttf',
			'fontcolor': '#000000'}
		html = requests.post(url=self.url,data=data,headers=self.headers)
		html_soup = BeautifulSoup(html.text,'lxml')
		img_url = self.url + html_soup.find('div',attrs={'class':'tu'}).find('img')['src'] 
		print(img_url)
		img_html = requests.get(url=img_url,headers=self.headers)
		img_html.encoding = 'utf8'
		self.down(img_html)

	def down(self,img_html):	# 下载图片
		f = open('{}.gif'.format(self.word),'wb')
		f.write(img_html.content)
		f.close()
		self.view_img()

	def view_img(self):		# GUI 展示
		image = PhotoImage(file='{}.gif'.format(self.word))
		label2 = Label(self.part,image=image)
		label2.bm = image
		label2.grid(row=3,columnspan=2)

	# def test(self):
	# 	return self.word

# spider = Spider()
# spider.post_img(word,fonts)


