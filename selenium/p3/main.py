from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

# articles= driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')

# articles.click()

# all_portals= driver.find_element(By.LINK_TEXT, value="Site news")
# all_portals.click()

search= driver.find_element(By.NAME,value="search")

search.send_keys("Arjun Thazhath BCE",Keys.ENTER)
