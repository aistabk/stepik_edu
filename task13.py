from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time
import math


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    button = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button.click()
    
    browser.switch_to.window(browser.window_handles[1])
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y= calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла