from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from threading import Thread 
import time 


chrome_options= webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

 
class EverySoOften(Thread): 
    def __init__(self, seconds): 
        '''Note that when you override __init__, you must  
           use super() to call __init__() in the base class 
           so you'll get all the "chocolately-goodness" of 
           threading (i.e., the magic that sets up the thread 
           within the OS) or it won't work. 
        '''         
        super().__init__()  
        self.delay = seconds 
        self.is_done = False 
 
    def done(self): 
        self.is_done = True 
 
    def run(self):
        while not self.is_done:
            time.sleep(self.delay)
            try:
                money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
            except ValueError:
                money = 0

            store_items = driver.find_elements(By.CSS_SELECTOR, "#store div[id^='buy']")
            
            affordable_items = []
            for item in store_items:
                if "grayed" not in item.get_attribute("class"):
                    try:
                        name, cost = item.text.split(" - ")
                        cost = int(cost.replace(",", ""))
                        affordable_items.append((cost, item))
                    except:
                        continue

            if affordable_items:
                # Buy the most expensive affordable item
                _, item_to_buy = max(affordable_items, key=lambda x: x[0])
                item_to_buy.click()
 
 
t = EverySoOften(2) 
t.start() 

cookie= driver.find_element(By.ID, value="cookie")

start_time = time.time()
while time.time() - start_time < 200:  # Run for 5 minutes
    cookie.click()

t.done() 
time.sleep(1)

cps_element = driver.find_element(By.ID, "cps")
print("CPS:", cps_element.text)


