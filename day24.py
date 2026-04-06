from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
search=driver.find_element(By.NAME,"q")
search.send_keys("Python automation")
search.submit()

button = driver.find_element(By.NAME, "btnK")
button.click()

print(driver.title)
driver.quit()
driver.maximize_window()


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com/login")

driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("1234")
