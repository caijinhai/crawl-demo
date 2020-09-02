from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Firefox driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Go to the Google home page
driver.get('https://www.baidu.com')

# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
        )
