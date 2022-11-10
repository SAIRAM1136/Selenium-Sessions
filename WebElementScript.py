import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
PageTitle = driver.title
print(PageTitle)

driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
# driver.find_element(By.NAME, 'txtUsername').send_keys("Admin")
# driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
# driver.find_element(By.CLASS_NAME, 'button').click()
# driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
# driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
# #driver.find_element(By.CSS_SELECTOR, "//input[type='password']").send_keys("admin123")
# driver.find_element(By.XPATH, "//input[@value='LOGIN']").click()
# print("After Login URL is :", driver.current_url)
# assert "dashboard" in driver.current_url
# driver.find_element(By.XPATH, "//a[contains(text(), 'Welcome')]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()
# print("After Logout URL is :", driver.current_url)
# assert "login" in driver.current_url
#
# driver.implicitly_wait(3)

#driver.quit()