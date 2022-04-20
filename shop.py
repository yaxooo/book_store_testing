# Shop: отображение страницы товара
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

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

# 2. Залогиньтесь
driver.implicitly_wait(5) # искать каждый элемент в течение 5 секунд
MyAccountMenu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
MyAccountMenu.click()
Email = driver.find_element_by_id('username')
Email.send_keys("2002tester@mail.ru")
Password = driver.find_element_by_id('password')
Password.send_keys("PlayBoy11!!PlayBoy11!!")
login = driver.find_element_by_name('login')
login.click()

# 3. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_id('menu-item-40')
Shop.click()

# 4. Откройте книгу "HTML 5 Forms"
HTML5Forms=driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
HTML5Forms.click()

# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
button = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'product_title.entry-title'), "HTML5 Forms"))
if button==False:
    print('Заголовок книги НЕ соднржит: "HTML5 Forms"')
else:
    print('Заголовок книги соднржит: "HTML5 Forms"')
time.sleep(5)

# Shop: количество товаров в категории
driver.get("http://practice.automationtesting.in/")

# # 2. Залогиньтесь
# driver.implicitly_wait(5) # искать каждый элемент в течение 5 секунд
# MyAccountMenu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
# MyAccountMenu.click()
# Email = driver.find_element_by_id('username')
# Email.send_keys("2002tester@mail.ru")
# Password = driver.find_element_by_id('password')
# Password.send_keys("PlayBoy11!!PlayBoy11!!")
# login = driver.find_element_by_name('login')
# login.click()

# 3. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_id('menu-item-40')
Shop.click()

# 4. Откройте категорию "HTML"
HTML=driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]')
HTML.click()

# 5. Добавьте тест, что отображается три товара
account_products=driver.find_elements_by_css_selector('[rel="nofollow"]')
if len(account_products)==3:
    print('На странице отображается: ', len(account_products))
else:
    print('На странице отображается не верное количество товаров: ', len(account_products))



# Shop: сортировка товаров
driver.get("http://practice.automationtesting.in/")

# # 2. Залогиньтесь
# driver.implicitly_wait(5) # искать каждый элемент в течение 5 секунд
# MyAccountMenu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
# MyAccountMenu.click()
# Email = driver.find_element_by_id('username')
# Email.send_keys("2002tester@mail.ru")
# Password = driver.find_element_by_id('password')
# Password.send_keys("PlayBoy11!!PlayBoy11!!")
# login = driver.find_element_by_name('login')
# login.click()

# 3. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_id('menu-item-40')
Shop.click()

# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
element=driver.find_element_by_class_name('orderby')
element_name = element.get_attribute("value")
if element_name=='menu_order':
    print("В селекторе выбран вариант сортировки по умолчанию: ", element_name)
else:
    print("В селекторе выбран НЕ правильный вариант: ", element_name)


# 5. Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
select = Select(element)
select.select_by_value("price-desc")

# 6. Снова объявите переменную с локатором основного селектора сортировки, т.к после сортировки страница обновится
element=driver.find_element_by_class_name('orderby')

# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value
element_name = element.get_attribute("value")
if element_name=='price-desc':
    print("В селекторе выбран вариант сортировки по цене от большей к меньшей: ", element_name)
else:
    print("В селекторе выбран НЕ правильный вариант: ", element_name)


# Shop: отображение, скидка товара    СЛАЙД 100
driver.get("http://practice.automationtesting.in/")

# # 2. Залогиньтесь
# driver.implicitly_wait(5) # искать каждый элемент в течение 5 секунд
# MyAccountMenu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
# MyAccountMenu.click()
# Email = driver.find_element_by_id('username')
# Email.send_keys("2002tester@mail.ru")
# Password = driver.find_element_by_id('password')
# Password.send_keys("PlayBoy11!!PlayBoy11!!")
# login = driver.find_element_by_name('login')
# login.click()

# 3. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_id('menu-item-40')
Shop.click()

# 4. Откройте книгу "Android Quick Start Guide"
AndroidQuickStartGuide = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
AndroidQuickStartGuide.click()

# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
old_price=driver.find_element_by_xpath("//p[@class='price']/del")
old_price_check = old_price.text
print('Старая цена:', old_price_check)
assert old_price_check == "₹600.00"

# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
new_price=driver.find_element_by_xpath("//p[@class='price']/ins")
new_price_check = new_price.text
print('Новая цена:', new_price_check)
assert new_price_check == "₹450.00"

# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки
# (не вся картинка на всю страницу)
img = WebDriverWait(driver, 5).until( EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single.size-shop_single.wp-post-image")) )
img.click()
time.sleep(3)

# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close = WebDriverWait(driver, 5).until( EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
close.click()



# Shop: проверка цены в корзине
# Открытие нового окна и выход из аккаунта
driver.execute_script("window.open();")
window_1 = driver.window_handles[1] # создание переменной, где укажем путь к второй вкладке
driver.switch_to.window(window_1) # переключим область действия драйвера на новую вкладку
driver.get("http://practice.automationtesting.in/")
MyAccountMenu = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]')
MyAccountMenu.click()
button_Logout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout')))
button_Logout.click()

# 2. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_id('menu-item-40')
Shop.click()

# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# если все книги будут out of stock - тогда пропустите это и следующие два задания
book = driver.find_element_by_css_selector('[data-product_id="182"]')
book.click()
time.sleep(3)

# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
basket= WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "wpmenucart-contents")))
basket_check = basket.text
print(basket_check)
assert basket_check == "1 Item₹180.00"

# 5. Перейдите в корзину
basket.click()

# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
Subtotal= WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]'), "180.00"))
print('В Subtotal отобразилась стоимость', Subtotal)

# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
Total= WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'strong'), "189.00"))
print('В Total отобразилась стоимость', Total)


time.sleep(5)
driver.quit()