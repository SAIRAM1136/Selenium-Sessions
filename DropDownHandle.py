import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser = Service("C:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.maximize_window()
driver.get("https://www.facebook.com")
PageTitle = driver.title
print(PageTitle)

driver.find_element(By.XPATH, "//a[contains(text() ,'Create New Account')]").click()

time.sleep(2)

month = driver.find_element(By.NAME, "birthday_month")
#select method object is created
Monthdd = Select(month)
List = Monthdd.options
print(len(List))

for ele in List:
    print(ele.text)
    if ele.text == "Sep":
        ele.click()
        break


# Monthdd.select_by_index(4)
# time.sleep(2)
# Monthdd.select_by_value('6')
# time.sleep(2)
# Monthdd.select_by_visible_text("Sep")




