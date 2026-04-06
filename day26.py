import pyautogui
pyautogui.moveTo(500,300)
pyautogui.click()
pyautogui.press("enter")
pyautogui.screenshot("screenshot.png")

import time
time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

links = driver.find_elements(By.TAG_NAME,"a")

for l in links:
    print(l.get_attribute("href"))
    
    
    import pyautogui
import time

time.sleep(5)

pyautogui.write("Hello this is automation",interval=0.1)


import pyautogui
import time

time.sleep(3)

pyautogui.press("win")
pyautogui.write("notepad")
pyautogui.press("enter")


