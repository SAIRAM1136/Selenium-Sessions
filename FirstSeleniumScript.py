from _ast import Assert

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Executable path has been deprecated so instead of that we are now using Service class by creating Object of that

ser = Service("C:\\drivers\\chromedriver.exe")

driver = webdriver.Chrome(service=ser)
print(type(driver))

driver.maximize_window()
driver.get("http://www.google.com")

PageTitle = driver.title

print(PageTitle)

#Validation
assert "Google" in PageTitle

driver.quit()

