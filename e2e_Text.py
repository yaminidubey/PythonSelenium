from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


crome_option = webdriver.ChromeOptions()
crome_option.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="/home/nishank/Downloads/chromedriver", options=crome_option)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(by=By.CSS_SELECTOR, value=("a[href*='shop']")).click()
products = driver.find_elements(by=By.XPATH, value=("//div[@class='card h-100']"))
for product in products:
    productname = product.find_element_by_xpath("div/h4/a").text
    if productname == "Blackberry":
        product.find_element_by_xpath("div/button").click()
        break

driver.find_element(by=By.CSS_SELECTOR, value=("a[class*='btn-primary']")).click()
driver.find_element(by=By.XPATH, value=("//button[@class='btn btn-success']")).click()
driver.find_element(by=By.ID, value= ("country")).send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(by=By.LINK_TEXT, value=("India")).click()
driver.find_element(by=By.XPATH, value=("//label[@for='checkbox2']")).click()
driver.find_element(by=By.XPATH,value=("//input[@value='Purchase']")).click()
print(driver.find_element(by=By.CLASS_NAME, value=("alert-success")).text)