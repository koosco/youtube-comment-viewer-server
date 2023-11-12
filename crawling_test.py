from selenium import webdriver 
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

 
display = Display(visible=0, size=(1024, 768)) 
display.start()
 
path = '/home/ubuntu/chromedriver' 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.naver.com/"
driver.get(url)
print(driver.page_source)

driver.quit()
