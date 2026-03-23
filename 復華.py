

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#%%

st_list = ["01", "03", "04", "05", "06", "07", "08", "10", "11", "12", "14", "16", "18", "19", "20", "21", "22", "23", "24", "25"]

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

df_output = pd.DataFrame()

for i in st_list:
    
    driver.get("https://www.fhtrust.com.tw/ETF/etf_detail/ETF" + i + "#brief")
    
    time.sleep(2)
    
    st_id = driver.find_element(By.XPATH, '//*[@id="app"]/main/section[1]/div[2]/div/div[1]/div[1]/p/span[1]')
    st_name = driver.find_element(By.XPATH, '//*[@id="app"]/main/section[1]/div[2]/div/div[1]/div[1]/p/span[2]')
    
    participate_company = pd.read_html("https://www.fhtrust.com.tw/ETF/etf_detail/ETF" + i + "#brief")[-1]
    participate_company = participate_company[1].iloc[-2]
    
    df_output_part = pd.DataFrame([st_id.text, st_name.text, participate_company]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, st_name, participate_company
    
   










