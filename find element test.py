import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/nishank/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for ch in countries:
    if ch.text == "India":
        ch.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

