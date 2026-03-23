from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()


st_list = ["49YTW", "46YTW", "61YTW", "50YTW", "47YTW", "44YTW", "37YTW", "36YTW"]

df_output = pd.DataFrame()

for i in st_list:
   
    driver.get("https://www.ezmoney.com.tw/ETF/Fund/Info?fundCode=" + i)
    
    time.sleep(2)
    
    
    participate_company_click = driver.find_element(By.XPATH, '//*[@id="fundApp"]/div[1]/div[4]/a[5]')
    participate_company_click.click()
    
    time.sleep(2)
    
    participate_company = driver.find_element(By.XPATH, '//*[@id="securities"]/div/div[2]')

    participate_company_str = ""
    
    for j in participate_company.text.split("\n"):
        
        if(j.split(" ")[0].find("證券") != -1):
            participate_company_str = participate_company_str + j.split(" ")[0] + "、"

    
    participate_company_str = participate_company_str[:-1]

    
    st_id = driver.find_element(By.XPATH, '//*[@id="fundApp"]/div[1]/div[3]/span[1]/span[1]') 
    st_name = driver.find_element(By.XPATH, '//*[@id="fundApp"]/div[1]/div[3]/span[1]/span[2]') 
    
    df_output_part = pd.DataFrame([st_id.text, st_name.text, participate_company_str]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, participate_company, participate_company_str
    
    
    
     
     
     
     
     
     
     
     