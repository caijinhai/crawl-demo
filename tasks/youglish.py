import requests
import time
import json
import urllib.request, http.cookiejar
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()
key = '******'
retry = 3


def test_v2_recaptcha():
	page_url = 'https://www.google.com/recaptcha/api2/demo'
	driver.get(page_url)
	time.sleep(5)

	google_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"

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
	google_key = 'f9630567-8bfa-4fc9-8ee5-9c91c6276dff'
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
	cookies = cookie_str.split(";")
	for c in cookies:
	    k,v = a.split("=")
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

	# cookie = http.cookiejar.CookieJar()
	# handler = urllib.request.HTTPCookieProcessor(cookie)
	# opener = urllib.request.build_opener(handler)
	# response = opener.open(page_url)

	# print(cookie)

	cookie_str = '__cfduid=d22c2b7fdab12394e3679d85eb71dbf5d1597923638; cf_chl_1=9de164e596c616f; cf_chl_prog=a19; cf_clearance=84e2074e526ab25d655c3d617a46fea94f562630-1597923664-0-1z53e24bdz56169e9z9d2734cc-250; JSESSIONID=8D9B1FBE3B6BFFF9680C631D31FBDC87; width=1614; _ga=GA1.2.2009944912.1597923668; _gid=GA1.2.678748583.1597923670; _gat=1; cookie_consent=1; __gads=ID=3d29180897a327b9:T=1597923673:S=ALNI_MaoD-x-VdL_GrZ4uJ__1rXsXaxtqw; history=27339844/retell/english'
	
	cj = http.cookiejar.CookieJar()
	cookies = cookie_str.split(";")
	for c in cookies:
	    k = c.split("=")[0]
	    v = c.split("=")[1]
	    cookie = http.cookiejar.Cookie(None, k, v, None, False, "", 
	                                   False, "", "",
	                                   False,False, False,False,
	                                   False,
	                                   "",
	                                   "",None)

	    cj.set_cookie(cookie)

	handler = urllib.request.HTTPCookieProcessor(cj)
	opener = urllib.request.build_opener(handler)
	response = opener.open(page_url)


if __name__ == '__main__':
	# youglish_cookie()
	# save_youlish_cookie()
	youglish_recaptcha()

