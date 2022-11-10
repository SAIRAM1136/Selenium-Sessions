import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser = Service("C:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.maximize_window()

driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.implicitly_wait(20)

driver.find_element(By.ID, 'tags').send_keys("S")
ListElements = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']//div")
print(len(ListElements))

for ele in ListElements:
    print(ele.text)

    if ele.text == "Selenium":
        ele.click()
        break


