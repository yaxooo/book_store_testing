# Shop: работа в корзине
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


# Shop: работа в корзине
# 2. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_id('menu-item-40')
Shop.click()

# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
book1 = driver.find_element_by_css_selector('[data-product_id="182"]')
book1.click()
time.sleep(2)
book2 = driver.find_element_by_css_selector('[data-product_id="180"]')
book2.click()


# 4. Перейдите в корзину
basket= WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "wpmenucart-contents")))
basket.click()

# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
time.sleep(2)
del_btn=driver.find_element_by_css_selector('[data-product_id="182"]')
del_btn.click()

# 6. Нажмите на Undo (отмена удаления)
Undo=driver.find_element_by_link_text('Undo?')
Undo.click()

# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
Quantity=driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
Quantity.clear()
Quantity.send_keys("3")

# 8. Нажмите на кнопку "UPDATE BASKET"
UpdateBasket=driver.find_element_by_css_selector('[value="Update Basket"]')
UpdateBasket.click()

#9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# используйте assert
Quantity=driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
Quantity_value=Quantity.get_attribute('value')
assert Quantity_value == "3"

# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
time.sleep(2)
APPLY_COUPON=driver.find_element_by_name('apply_coupon')
APPLY_COUPON.click()

# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
text= WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
if text==True:
    print('Сообщение "Please enter a coupon code." появилось')
else:
    print('Сообщение не появилсь')

time.sleep(3)
driver.quit()