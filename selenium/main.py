from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options= webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")


search_bar=driver.find_element(By.NAME,value="q")
print(search_bar.get_attribute("placeholder"))


go_button= driver.find_element(By.ID,value="submit")
print(go_button.size)


# documentation_link= driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

documentation_link= driver.find_element(By.CSS_SELECTOR, value=".small-widget.documentation-widget a") 
print(documentation_link.text)

bug_link= driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

print(bug_link.text)

# driver.close()
driver.quit()