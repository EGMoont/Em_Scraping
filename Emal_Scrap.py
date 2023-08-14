#Introduction of libraries

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pandas as pd

#Webdriver used to open chrome automaticlly
driver = webdriver.Chrome(executable_path=r"C:/Chrome/chromedriver.exe")
driver.get("https://emalls.ir/%D9%85%D8%AD%D8%B5%D9%88%D9%84%D8%A7%D8%AA~Category~39")
driver.minimize_window()

# time.sleep(20)

Mobile_Names = []
Mobile_Price = []

#Finding names and price by xpath
 
All_Product =driver.find_elements(By.XPATH,'//div[@class="product-block-parent"]')

for product in All_Product:
    names = driver.find_elements(By.XPATH,'//a[@class="prd-name"]')
    for name in names:
        Mobile_Names.append(name.text)

    prices = driver.find_elements(By.XPATH,'//div[@class="prd-price"]')
    for price in prices:
        Mobile_Price.append(price.text)

    # time.sleep(20)

#Saving data in exel format
ds =pd.DataFrame(zip(Mobile_Names,Mobile_Price),columns=['Names','Prices'])
ds.to_excel(r"Emalls_Mobile.xlsx",index=False)




