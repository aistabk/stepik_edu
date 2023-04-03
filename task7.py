from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y= calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control:required")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
	
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

#html body.bg-light div.container form div.form-group label span#input_value.nowrap