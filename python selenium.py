import time

from selenium import webdriver

#driver = webdriver.Chrome(executable_path="/home/nishank/Downloads/chromedriver")
driver = webdriver.Firefox(executable_path="/home/nishank/Downloads/geckodriver")
driver.maximize_window()
driver.get("https://www.youtube.com/")
time.sleep(3)
print(driver.title)
print(driver.current_url)
driver.get("https://www.fb.com/")
driver.back()
time.sleep(3)

driver.close()