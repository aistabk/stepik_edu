from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

#price = browser.find_element(By.ID, "price")
button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"100")
)
button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y= calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла