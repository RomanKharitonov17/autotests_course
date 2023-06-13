# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

login = 'Login220621'
password = 'Login220621Login220621'
browser = webdriver.Chrome()
fix = 'https://fix-online.sbis.ru/'
dialogs = 'https://fix-online.sbis.ru/page/dialogs'
message = 'test'

try:
    # Авторизация
    browser.get(fix)
    time.sleep(1)
    browser.find_element(By.NAME, 'Login').send_keys(login, Keys.ENTER)
    time.sleep(1)
    browser.find_element(By.NAME, 'Password').send_keys(password + Keys.ENTER)
    time.sleep(3)

    # Контакты
    browser.get(dialogs)
    time.sleep(.3)

    # Cообщение
    plus_btn = browser.find_element(By.CLASS_NAME, 'sabyPage-MainLayout__addButton')
    plus_btn.click()
    time.sleep(2)
    fio_field = browser.find_elements(By.CSS_SELECTOR, '.controls-InputBase__nativeField_hideCustomPlaceholder')
    fio_field[0].send_keys('Харитонов Роман Александрович', Keys.ENTER)
    time.sleep(2)
    admin_find = browser.find_element(By.CSS_SELECTOR, '.person-Info__withActivity')
    admin_find.click()
    time.sleep(2)
    message_text = browser.find_element(By.CSS_SELECTOR, '.textEditor_slate_Container')
    time.sleep(2)
    message_text.send_keys(message)
    yes_btn = browser.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    yes_btn.click()
    time.sleep(3)

    # Проверка появления сообщения
    sent_messages = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert sent_messages[0].text == message

    # Удаление сообщения
    action_chain = ActionChains(browser)
    action_chain.move_to_element(sent_messages[0])
    action_chain.perform()
    delete_btn = browser.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_btn.click()
    time.sleep(3)

    # Проверка удаления
    assert browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')[0] != sent_messages[0]
    time.sleep(3)
finally:
    browser.quit()
