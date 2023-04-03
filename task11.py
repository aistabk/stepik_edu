from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("firstname")  
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("lastname")  
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("email")
    
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #file_path = os.path.join(current_dir, "text.txt")           
    file_name = "text.txt"
    file_path = os.path.join(current_dir, "text.txt")   
    element = browser.find_element(By.CSS_SELECTOR, "html body.bg-light div.container form input#file")
    element.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    
    
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
