

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#%%

st_list = ["20", "17", "21", "22", "23", "18", "19", "15", "16", "02", "03", "04", "05", "06", "07", "09", "14"]

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

df_output = pd.DataFrame()

for i in st_list:
    
    driver.get("https://www.kgifund.com.tw/Fund/Detail?fundID=J0" + i)
    
    time.sleep(2)
    
    st_id = driver.find_element(By.XPATH, '//*[@id="ETFInfo"]/div/div[2]/ul/li[1]/span[2]')
    st_name = driver.find_element(By.XPATH, '//*[@id="ETFInfo"]/div/div[2]/ul/li[2]/span[2]')
    
    participate_company = driver.find_element(By.XPATH, '//*[@id="IndexIntroduction"]/div/div[2]/ul/li[7]/span[2]')
    
    df_output_part = pd.DataFrame([st_id.text, st_name.text, participate_company.text]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, st_name, participate_company
    
    
    
    


