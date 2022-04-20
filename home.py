# Home: добавление комментария
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Код для включения AdBlock
path_to_extension = r' C:\Users\Админ\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.44.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")

# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
driver.implicitly_wait(5) # искать каждый элемент в течение 5 секунд

# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
SeleniumRuby = driver.find_element_by_css_selector('[alt="Selenium Ruby"]')
SeleniumRuby.click()

# 4. Нажмите на вкладку "REVIEWS"
REVIEWS = driver.find_element_by_css_selector('[href="#tab-reviews"]')
REVIEWS.click()

# 5. Поставьте 5 звёзд
Rating = driver.find_element_by_class_name('star-5')
Rating.click()
time.sleep(5)

# 6. Заполните поле "Review" сообщением: "Nice book!"
Review = driver.find_element_by_id('comment')
Review.send_keys("Nice book!")

# 7. Заполните поле "Name"
Name = driver.find_element_by_id('author')
Name.send_keys("Kate")

# 8. Заполните "Email"
Email = driver.find_element_by_id('email')
Email.send_keys("2002tester@mail.ru")

# # 9. Нажмите на кнопку "SUBMIT"
SUBMIT = driver.find_element_by_id('submit')
SUBMIT.click()

time.sleep(5)
driver.quit()