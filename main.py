from cmath import log, tan
from lib2to3.pgen2 import driver
from msilib.schema import tables
from operator import imod
from pathlib import Path
from pydoc import HTMLDoc
from re import A
from tkinter.tix import MAX
from traceback import print_tb
import numpy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.support.ui import Select
import pandas as pd

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)


r = requests.get(
    'https://www.camara.cl/legislacion/ProyectosDeLey/tramitacion.aspx?prmID=12616&prmBoletin=12100-07')
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs={'class': 'paginacion aleft'})

pagJurista = table.find("span")
pagJurista = pagJurista.get_text()


def ListDeElementosTable():
    
    inicial = "ContentPlaceHolder1_ContentPlaceHolder1_ContentPlaceHolder1_pager_rptPager_current_0"


    Anterior = 0
    pagList = [1]
    pagList.append(inicial)

    for x in pagJurista:
        if(x != " " and x != 13 and x != 8):
            try:
                y = int(x)
                if(type(y) == int  and Anterior < y):
                    pag = soup.find(id ="ContentPlaceHolder1_ContentPlaceHolder1_ContentPlaceHolder1_pager_rptPager_page_{}".format(y))
                    Anterior = y
                    pagList.append(pag.text)
                    
            except ValueError:
                pass
            print(pagList[-1])
    return pagList[-1]                




def selenium(index):
    driver.get("https://www.camara.cl/legislacion/ProyectosDeLey/tramitacion.aspx?prmID=12616&prmBoletin=12100-07")
    if(index != "1"):
        paginacion_aleft = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_ContentPlaceHolder1_pager_rptPager_page_{}".format(index))
        paginacion_aleft.click()
        print("IF")
        time.sleep(3)

    
    soup = BeautifulSoup(driver.page_source)
    soup_table = soup.find_all("table")[-1]
    soup_table = soup.find("table")
    tables = pd.read_html(str(soup_table))
    print(tables)
    #driver.quit()    


selenium("7") # INDICE 8 desface de x+1

