from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()


st_list = [176, 173, 162, 131, 130]

df_output = pd.DataFrame()

for i in st_list:
    
   
    driver.get("https://www.ftft.com.tw/etf/product/details/?id=" + str(i) + "&tab=market")
    
    time.sleep(2)
    
    participate_company = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]')
    

    participate_company_str = ""
    
    for j in participate_company.text.split("\n")[1:]:
        
        participate_company_str = participate_company_str + j + "、"

    
    participate_company_str = participate_company_str[:-1]

    
    st_id = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/p[1]')  
    st_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/h3')
    

    df_output_part = pd.DataFrame([st_id.text, st_name.text.split("★ ")[1], participate_company_str]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, st_name, participate_company, participate_company_str
    
    
    
     
     
     
     
     
     
     
     