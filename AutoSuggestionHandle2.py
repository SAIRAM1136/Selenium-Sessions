import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
driver.maximize_window()

driver.get("https://www.google.com/")
driver.implicitly_wait(20)

driver.find_element(By.NAME, 'q').send_keys("Mukesh Otwani")
ListElements = driver.find_elements(By.XPATH, "//ul[(@class='G43f7e')]//div[@class='wM6W7d']//span")
print(len(ListElements))
for ele in ListElements:
    print(ele.text)

    if ele.text == "mukesh otwani youtube":
        ele.click()
        break

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//h3[contains(text(), 'Mukesh otwani - YouTube')]").click()
time.sleep(3)

driver.quit()
