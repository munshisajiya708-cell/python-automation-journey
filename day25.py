from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://google.com")

wait = WebDriverWait(driver,10)
search = wait.until(EC.presence_of_element_located((By.NAME,"q")))

search.send_keys("Python automation jobs")
search.submit()
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")

driver.execute_script("window.open('https://youtube.com')")

tabs = driver.window_handles
driver.switch_to.window(tabs[1])



