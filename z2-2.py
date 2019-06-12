







import requests #парсит код html и возвращает в функцую которую скажут
from bs4 import Beautifulsoup4 #парсинг

def get_html(url):
	r = requests.get(url) #response
	return r.text         #возвращает html

def get_all_links(html, 'lxml'):
	soup = Beautifulsoup(html) 





def main():
	#https://coinmarketcap.com/all/views/all/
	all_links = []










if __name__ '__main__':
	main()