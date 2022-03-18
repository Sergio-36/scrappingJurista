from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\msedgedriver.exe'

driver = webdriver.Edge(PATH)

driver.get("https://www.senado.cl/appsenado/templates/tramitacion/index.php?boletin_ini=13626-03")
assert "Senado - Tramitación de proyectos" in driver.title
content = driver.find_element_by_class_name('ev_modern')


