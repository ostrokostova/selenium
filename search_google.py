import time # подключение модуля для работы со временем
from selenium import webdriver # подключение webdriver для управления браузером
driver = webdriver.Chrome()# инициализируется драйвер браузера. После этой команды должно открыться новое окно браузера
time.sleep(5) # команда time.sleep устанавливает паузу в 5 секунд, чтобы успеть увидеть, что происходит в браузере
driver.get("https://google.com")# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(5)
searche_input = driver.find_element_by_name("q")
time.sleep(5)
searche_input.send_keys("АГУ")
button_input = driver.find_element_by_tag_name("form").submit()
time.sleep(5)
driver.quit()# После выполнения всех действий надо закрыть окно браузера