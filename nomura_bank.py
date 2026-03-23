from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#%%

st_list = ["00935", "00944", "00960", "00971", "00972", "00980A", "00985A", "009812", "00987B", "00999A"]

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

df_output = pd.DataFrame()

for i in st_list:
    
    driver.get("https://www.nomurafunds.com.tw/ETFWEB/product-description?fundNo=" + i + "&tab=basic")
    
    time.sleep(1)
    
    st_id = driver.find_element(By.XPATH, '//*[@id="basic"]/div[1]/div[1]/div/div[1]/div/div/p[2]')
    st_name = driver.find_element(By.XPATH, '//*[@id="basic"]/div[1]/div[1]/div/div[2]/div/div/p[2]')
    participate_company = driver.find_element(By.XPATH, '//*[@id="basic"]/div[1]/div[3]/div/div[1]/div/div/p[2]')
    
    
    df_output_part = pd.DataFrame([st_id.text, st_name.text, participate_company.text]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, st_name, participate_company