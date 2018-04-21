from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())


# BeautifulSoup是一个python的第三方库，它的基本功能就是把获取的html的整个页面变成一个对象，
# 然后我们可以通过对象的属性(html标签)来获取标签和其中的内容。
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),"lxml")
print(bsObj.h1)           # 例如获取该页面的h1标签和其内容


# urlopen通常会出现两种异常，第一种是网页在服务器不存在(或者获取页面是出现错误)，第二种是服务器不存在。
from urllib.error import HTTPError
def getTitle(url):																		# 可以返回页面标题的函数
	try:
		html = urlopen("http://www.pythonscraping.com/pages/page1.html")				# 当发生上面两种异常就返回None对象
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(),"lhtml")										# 当获取该网页(没有发生异常)
		title = bsObj.body.h1															# 如果你想调用的标签不存在bs对象就会返回None，这时候不会报错。
	except AttributeError as e:															# 但是如果还要继续调用None下面的标签就会出现AttriobuteError
		return None
	return title
	title = getTitle("http://www.pythonscraping.com/pages/page1.html")					# 我们也可以使用bs的通用函数去获取标签
	if title == None:
		print("Title could not be found")
	else:
		print(title)