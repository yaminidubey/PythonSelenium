from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/nishank/Downloads/chromedriver (2)")
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("1990.nishank.tripathi@gmail.com")
driver.find_element_by_id("pass").send_keys("Yamini90#")
driver.find_element_by_id("pass").clear()

#driver.find_element_by_xpath("//button[@name='login']").click()

driver.find_element_by_link_text("Forgotten password?").click()

driver.find_element_by_xpath("//a[text()= 'Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/button1").text)
print(driver.find_elements_by_css_selector("form[name='login'] .div:nth_child(1)").test)


