import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/nishank/Downloads/chromedriver")
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
driver.find_elements_by_xpath("//div[@class='products']/div[@class='product']")
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_css_selector("span.promoinfo").text)

