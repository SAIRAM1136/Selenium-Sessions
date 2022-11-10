from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()

driver.get("https://our.intern.facebook.com/intern/oculus/oculus_bug_maker/Stella/")
driver.implicitly_wait(20)

driver.find_element(By.ID, "email").send_keys("srbee@fb.com")
driver.find_element(By.ID, "pass").send_keys("hcloculus@12345")

driver.find_element(By.ID, "loginbutton").click()