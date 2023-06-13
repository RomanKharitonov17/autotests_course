# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
sbis_url = 'https://sbis.ru'
tensor_url = 'https://tensor.ru'
tensor_about = 'https://tensor.ru/about'
try:
    browser.get(sbis_url)
    time.sleep(1)
    contact = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contact.click()
    time.sleep(1)
    browser.get(tensor_url)
    time.sleep(1)
    block = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert block.is_displayed()
    details = block.find_element(By.CSS_SELECTOR, '.tensor_ru-link')
    time.sleep(1)
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", btn2)
    time.sleep(1)
    assert details.is_displayed()
    details.click()
    time.sleep(1)
    assert browser.current_url == tensor_about
finally:
    browser.quit()

