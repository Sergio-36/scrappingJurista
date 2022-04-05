from asyncio.windows_events import NULL
from lib2to3.pgen2 import driver
from msilib.schema import tables
from pathlib import Path
from pydoc import HTMLDoc
from re import A
from tkinter.tix import MAX
import numpy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.support.ui import Select
import pandas as pd

#EXCEL
ipath = 'main\Seguimiento legislativo.xlsx'
df = pd.read_excel(ipath)
df["Flag"] = pd.NaT

def ListDeElementosTable(url):
    pagList = [1]
    try:
        r = requests.get("{}".format(url))
        soup = BeautifulSoup(r.content, 'html5lib')
        table = soup.find('div', attrs={'class': 'paginacion aleft'})
        pagJurista = table.find("span")
        pagJurista = pagJurista.get_text()

        Anterior = 0
        
        for x in pagJurista:
            if(x != " " and x != 13 and x != 8):
                try:
                    y = int(x)
                    if(type(y) == int  and Anterior < y):
                        pag = soup.find(id ="ContentPlaceHolder1_ContentPlaceHolder1_ContentPlaceHolder1_pager_rptPager_page_{}".format(y))
                        Anterior = y
                       # print(pagList)
                        try:
                            pagList.append(pag.text)
                        except:
                            pass
                        
                except ValueError:
                    pass

    except:
        pass
    return pagList[-1]               



def selenium(index,url,i):
      
    PATH = "C:\Program Files (x86)\msedgedriver.exe"
    driver = webdriver.Edge(PATH)
   
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        driver.get(url)
        table = soup.find('div', attrs={'class': 'paginacion aleft'})
        print("LOG : TRY")
        print(driver.get(url))
        pagJurista = table.find("span")
        pagJurista = pagJurista.get_text()
        print(index is not 1)
        time.sleep(5)
        
        
        if(index is not 1):
                paginacion_aleft = driver.find_element(By.ID, "ContentPlaceHolder1_ContentPlaceHolder1_ContentPlaceHolder1_pager_rptPager_page_{}".format(index))
                paginacion_aleft.click()
                print("IF")


        soup = BeautifulSoup(driver.page_source)
        print(url)
        print(soup)
        soup_table = soup.find_all("table")[-1]
        soup_table = soup.find("table")
        tables = pd.read_html(str(soup_table))
        dataf = tables[-1]
        # FECHA EXCEL = FECHA WEB
        df.iloc[i,9] =  dataf.iloc[len(dataf)-1][0]
        # ULTIMO MOVIMIENTO EXCEL = ULTIMO MOVIMIENTO WEB "Sub-etapa"
        df.iloc[i,7] = dataf.iloc[len(dataf)-1][3] 
        print(dataf.iloc[len(dataf)-1][3])
        #TRAMITE EXCEL = ETAPA WEB
        df.iloc[i,5] = dataf.iloc[len(dataf)-1][2] 
        #FLAG
        df.iloc[i,11] = "Update"

    except:
        df.iloc[i,11] = "Error"
        pass
    driver.quit() 










for i in df.index: 
    ultimoMovimiento = df.iloc[i,8]
    fechaUltimoMovimiento = df.iloc[i,9]
    url = df.iloc[i,10]
    index = (ListDeElementosTable(url))
   # print("INDEX :", type(index))
   # print("URL WHILE:  ",url  , type(url))
    selenium(str(index),url,i)
    i = i +1 

df.to_excel("output.xlsx") 