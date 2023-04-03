from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y= calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    
  
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
	
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

#html body.bg-light div.container form div.form-group label span#input_value.nowrap