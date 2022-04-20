# Registration_login: регистрация аккаунта
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

# 2. Нажмите на вкладку "My Account Menu"
driver.implicitly_wait(5) # искать каждый элемент в течение 5 секунд
MyAccountMenu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
MyAccountMenu.click()

# 3. В разделе "Register", введите email для регистрации
Email = driver.find_element_by_id('reg_email')
Email.send_keys("2002tester@mail.ru")

# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
Password = driver.find_element_by_id('reg_password')
Password.send_keys("PlayBoy11!!PlayBoy11!!")
time.sleep(5)

# 5. Нажмите на кнопку "Register"
Register = driver.find_element_by_name('register')
Register.click()
time.sleep(10)



# Registration_login: логин в систему
# 2. Нажмите на вкладку "My Account Menu"
driver.get("http://practice.automationtesting.in/")
MyAccountMenu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
MyAccountMenu.click()

# 3. В разделе "Login", введите email для логина
Email = driver.find_element_by_id('username')
Email.send_keys("2002tester@mail.ru")

# 4. В разделе "Login", введите пароль для логина
Password = driver.find_element_by_id('password')
Password.send_keys("PlayBoy11!!PlayBoy11!!")

# 5. Нажмите на кнопку "Login"
login = driver.find_element_by_name('login')
login.click()

# 6. Добавьте проверку, что на странице есть элемент "Logout"
button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout')))
if button==False:
    print('На странице НЕТ элемента "Logout"')
else:
    print('На странице есть элемент "Logout"')

time.sleep(5)
driver.quit()