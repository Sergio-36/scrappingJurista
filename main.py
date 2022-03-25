from cmath import log, tan
from lib2to3.pgen2 import driver
from msilib.schema import tables
from operator import imod
from pathlib import Path
from pydoc import HTMLDoc
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.support.ui import Select


PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

r = requests.get(
    'https://www.camara.cl/legislacion/ProyectosDeLey/tramitacion.aspx?prmID=12616&prmBoletin=12100-07')
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs={'class': 'paginacion aleft'})

pagJurista = table.find("span")
pagJurista = pagJurista.get_text()


def nextpag():
    
    pagList = []
    for x in pagJurista:
        if(x != " " and x != 13 and x != 8):
            try:
                y = int(x)
                if(type(y) == int):
                    pag = soup.find(id ="ContentPlaceHolder1_ContentPlaceHolder1_ContentPlaceHolder1_pager_rptPager_page_{}".format(y))
                    pagList.append(pag)
                    print(pag)
            except ValueError:
                pass
    return pagList                

def selenium():
    driver.get("https://www.camara.cl/legislacion/ProyectosDeLey/tramitacion.aspx?prmID=12616&prmBoletin=12100-07")
    
    paginacion_aleft = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_ContentPlaceHolder1_pager_rptPager_page_2")
    paginacion_aleft.click()

  