# Shop: покупка товара
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


# Shop: покупка товара
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
Shop = driver.find_element_by_id('menu-item-40')
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")

# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
book1 = driver.find_element_by_css_selector('[data-product_id="182"]')
book1.click()
time.sleep(2)

# 4. Перейдите в корзину
basket= WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "wpmenucart-contents")))
basket.click()

# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
checkout= WebDriverWait(driver, 5).until( EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.alt.wc-forward")) )
checkout.click()

# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода
#   - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё,
#   затем на вариант в списке ниже
first_name= WebDriverWait(driver, 5).until( EC.visibility_of_element_located((By.ID, "billing_first_name")) )
first_name.send_keys("Kate")
last_name= WebDriverWait(driver, 5).until( EC.visibility_of_element_located((By.ID, "billing_last_name")) )
last_name.send_keys("Shuv")
email= WebDriverWait(driver, 5).until( EC.visibility_of_element_located((By.ID, "billing_email")) )
email.send_keys("2002tester@mail.ru")
phone= WebDriverWait(driver, 5).until( EC.visibility_of_element_located((By.ID, "billing_phone")) )
phone.send_keys("1234567890")
# Country= driver.find_element_by_class_name('select2-choice')
# Country.click()
# CountryInp= driver.find_element_by_class_name('select2-input')
# CountryInp.send_keys("Bru")
# Country= WebDriverWait(driver, 5).until( EC.visibility_of_element_located((By.LINK_TEXT, "Brunei")) )
# Country.click()
address= driver.find_element_by_id('billing_address_1')
address.send_keys("Saint-Petesburg")
city= driver.find_element_by_id('billing_city')
city.send_keys("Saint-Petesburg")
postcode= driver.find_element_by_id('billing_postcode')
postcode.send_keys("197374")
state= driver.find_element_by_id('billing_state')
state.send_keys("Saint-Petesburg")

# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
CheckPayments= driver.find_element_by_id('payment_method_cheque')
CheckPayments.click()

# 8. Нажмите PLACE ORDER
place_order= driver.find_element_by_id('place_order')
place_order.click()

# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
text= WebDriverWait(driver, 5).until( EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),'Thank you. Your order has been received.') )
print('Надпись "Thank you. Your order has been received." отображается <----', text)

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
text= WebDriverWait(driver, 5).until( EC.text_to_be_present_in_element((By.CLASS_NAME, "shop_table.order_details"),'Check Payments') )
print('В Payment Method отображается текст "Check Payments" <----', text)

time.sleep(2)
driver.quit()