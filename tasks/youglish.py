import requests
import time
import json
import os
import xlrd
import urllib.request, http.cookiejar
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# driver = webdriver.Chrome(ChromeDriverManager().install())
# 使用已打开的浏览器窗口
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver = webdriver.Chrome()
key = '******'
retry = 3


def test_v2_recaptcha():
	page_url = 'https://www.google.com/recaptcha/api2/demo'
	driver.get(page_url)
	time.sleep(5)

	google_key = "**************"

	id = create_recaptcha_task_v2(page_url, google_key)
	if not id:
		print('no id, then return')
		return

	token = get_recaptcha_task_token(id)
	if not token:
		print('no token, then return')
		return

	# driver.find_element_by_xpath('//*[@id="checkbox"]').click()
	# time.sleep(3)
	# driver.find_element_by_xpath('//*[@id="checkbox"]').click()
	# token = '03AGdBq27J9t-9EBIkEiltnnvCHfztQwDZAqvPCXDDqZ8jY45Af50csyXMUfCmopOBNIyqZRJVW1ukY-6SKFObvtSxqkfT1QFPmrutSCGpSEbkdF1BcTGJfzSKAb4lhORheScFoUDOu6D-3uWQ5ek_A2dpO1xdkmuLSFaXMVV4mjihZJWtSDwOLqYLzY8VBrdtq2y2oW4k6bS5gN1V3LGbaWbZtyVw-iEtcCrxTx6Pq8lagm_g-pV-8QDGms03ujTX6ecm6m0v8KslsojsY-L9EDco0mdggYijf1ysvRPHmJFEvnQr7U2wBE3JP-QRa11W3voNDDrnaJgBM1K-n6VRqN5xHboaigVVPUJKBY6VhEst-N_t0ST5ZKZzwU1oMCEpURIja4B4zSJdQbQQwGfbqiYWvVi_2SRdAQ'
	element = driver.find_element_by_id('g-recaptcha-response')
	driver.execute_script("arguments[0].innerText = '%s'" % token, element)
	driver.find_element_by_id('recaptcha-demo-submit').click()

	time.sleep(3)

	driver.close()
	driver.quit()


def create_recaptcha_task_v2(page_url, google_key):
	i = 0
	while i < retry:
		res = requests.post('https://2captcha.com/in.php', data={
			"key": key,
			"method": "userrecaptcha",
			"googlekey": google_key,
			"pageurl": page_url,
			"json": 1
		})
		if res.json().get('status') == 1:
			return res.json().get('request')
		else:
			print('try fail %s: 3 seconds after try again! res: %s' % (i+1, json.dumps(res.json())))
			time.sleep(3)
			i += 1
	return ''

def create_recaptcha_task_v3(page_url, google_key):
	i = 0
	while i < retry:
		res = requests.post('https://2captcha.com/in.php', data={
			"key": key,
			"method": "userrecaptcha",
			"googlekey": google_key,
			"pageurl": page_url,
			"version": "v3",
			"action": "verify",
			"min_score": 0.3,
			"json": 1
		})
		if res.json().get('status') == 1:
			return res.json().get('request')
		else:
			print('try fail %s: 3 seconds after try again! res: %s' % (i+1, json.dumps(res.json())))
			time.sleep(3)
			i += 1
	return ''

def create_hcaptcha_task(page_url, google_key):
	i = 0
	while i < retry:
		res = requests.post('https://2captcha.com/in.php', data={
			"key": key,
			"method": "hcaptcha",
			"sitekey": google_key,
			"pageurl": page_url,
			"json": 1
		})
		if res.json().get('status') == 1:
			return res.json().get('request')
		else:
			print('try fail %s: 3 seconds after try again! res: %s' % (i+1, json.dumps(res.json())))
			time.sleep(3)
			i += 1
	return ''


def get_recaptcha_task_token(id):
	i = 0
	while i < retry:
		res = requests.get('https://2captcha.com/res.php', params={
			"key": key,
			"action": "get",
			"id": id,
			"json": 1
		})
		if res.json().get('status') == 1:
			return res.json().get('request')
		else:
			print('try fail %s: 60 seconds after try again! res: %s' % (i+1, json.dumps(res.json())))
			time.sleep(60)
			i += 1
	return ''


def youglish_recaptcha():
	google_key = '******************'
	search_word = 'retell'
	page_url = 'https://youglish.com/pronounce/%s/english/all' % search_word

	driver.get(page_url)
	time.sleep(5)

	# id = create_hcaptcha_task(page_url, google_key)
	# if not id:
	# 	print('no id, then return')
	# 	return
	# print("request_id: %s" % id)

	# token = get_recaptcha_task_token(id)
	# if not token:
	# 	print('no token, then return')
	# 	return

	# g = driver.find_element_by_name('g-recaptcha-response')
	# driver.execute_script("arguments[0].innerText = '%s'" % token, g)

	# h = driver.find_element_by_name('h-captcha-response')
	# driver.execute_script("arguments[0].innerText = '%s'" % token, h)
	# print(token)

	# print(driver.find_element_by_class_name('challenge-form'))
	# driver.find_element_by_class_name('challenge-form').click()
	# time.sleep(3)
	# driver.fid_element_by_class_name('challenge-form').click()
	# driver.get(page_url)	

	# time.sleep(20)

	# youtube_url = driver.find_element_by_id('player').get_attribute('src')

	# print(youtube_url)

	# driver.close()
	# driver.quit()

def youglish_cookie():
	cookie_str = '__cfduid=d22c2b7fdab12394e3679d85eb71dbf5d1597923638; cf_chl_1=9de164e596c616f; cf_chl_prog=a19; cf_clearance=84e2074e526ab25d655c3d617a46fea94f562630-1597923664-0-1z53e24bdz56169e9z9d2734cc-250; JSESSIONID=8D9B1FBE3B6BFFF9680C631D31FBDC87; width=1614; _ga=GA1.2.2009944912.1597923668; _gid=GA1.2.678748583.1597923670; _gat=1; cookie_consent=1; __gads=ID=3d29180897a327b9:T=1597923673:S=ALNI_MaoD-x-VdL_GrZ4uJ__1rXsXaxtqw; history=27339844/retell/english'
	
	cj = http.cookiejar.CookieJar()
	cookies = cookie_str.split("c s
	for c in cookies:
	    k,v = c.split("=")
	    cookie = http.cookiejar.Cookie(None, k, v, None, False, "", 
	                                   False, "", "",
	                                   False,False, False,False,
	                                   False,
	                                   "",
	                                   "",None)

	    cj.set_cookie(cookie)


	search_word = 'retell'
	page_url = 'https://youglish.com/pronounce/%s/english/all' % search_word

	driver.get(page_url)
	time.sleep(5)

	for item in cookie_str.split(';'):
		driver.add_cookie({"name":item.split('=')[0].strip(), "value": item.split('=')[1].strip()})

	print(driver.get_cookies())

	driver.get(page_url)
	time.sleep(5)

	youtube_url = driver.find_element_by_id('player').get_attribute('src')

	print(youtube_url)


def save_youlish_cookie():
	page_url = 'https://youglish.com/pronounce/retell/english/all'

	cookie = http.cookiejar.CookieJar()
	handler = urllib.request.HTTPCookieProcessor(cookie)
	opener = urllib.request.build_opener(handler)
	response = opener.open(page_url)

	print(cookie)

def driver_opened_chrome():
	page_url = 'https://youglish.com/pronounce/retell/english/all'

	dir = os.path.dirname(os.path.abspath(__file__))
	output_dir = os.path.join(dir, 'output')

	words = get_words(dir)
	print("total words: %s" % len(words))
	for word in words:
		url = 'https://youglish.com/fetch.jsp?vers=4&ts=3404236315972923746306&qp=0&lg=0&accent=0&nagla=1&query=%s' % word
		driver.get(url)

		json_str = driver.find_element_by_tag_name('pre').get_attribute('innerText')
		word_file = os.path.join(output_dir, '%s.json' % word)
		
		with open(word_file, 'w+') as f:
			f.write(json_str.strip())
		
		time.sleep(2)


def get_words(dir):
		file = os.path.join(dir, 'word.xlsx')
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		words = []
		for rx in range(sheet.nrows):
			if rx > 0:
				row = sheet.row(rx)
				words.append(row[0].value.strip())
		return words

if __name__ == '__main__':
	# youglish_cookie()
	# save_youlish_cookie()
	# youglish_recaptcha()
	driver_opened_chrome()

