import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser = Service("C:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.maximize_window()

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(20)

driver.find_element(By.ID, 'datepicker').click()
#driver.find_element(By.XPATH, "//a[text() = '25']").click()

Dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
print(len(Dates))

for ele in Dates:
    CurrentDate = ele.text
    print(CurrentDate)

    if CurrentDate == '24':
        ele.click()
        break

time.sleep(3)
driver.quit()