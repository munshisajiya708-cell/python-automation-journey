import schedule
import time

def job():
    print("Task running...")

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    import schedule,time

def task():
    print("Running")

schedule.every(2).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
    import schedule,time

def task():
    print("Running")

schedule.every(2).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

import schedule,time

def run_script():
    print("Script executed")

schedule.every(5).seconds.do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    import pyautogui,schedule,time

def screenshot():
    pyautogui.screenshot("daily.png")

schedule.every().day.at("12:00").do(screenshot)

while True:
    schedule.run_pending()
    time.sleep(1)    