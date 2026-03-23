from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#%%

st_list = [5, 16, 17, 18, 19, 20, 21, 22]

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

df_output = pd.DataFrame()

for i in st_list:
    
    driver.get("https://www.megafunds.com.tw/MEGA/etf/etf_product.aspx?id=" + str(i))
    
    time.sleep(2)
    
    st_id = driver.find_element(By.XPATH, '//*[@id="form"]/div[4]/div[1]/div[2]/div[7]/div[2]')
    st_name = driver.find_element(By.XPATH, '//*[@id="form"]/div[4]/div[1]/div[2]/div[1]/div[2]')
    participate_company = driver.find_element(By.XPATH, '//*[@id="nwt_content_1"]')
    
    participate_company_str = ""

    for j in participate_company.text.split("\n"):
        
        if(j.split(" ")[0].find("證券") != -1):
            participate_company_str = participate_company_str + j.split(" ")[0] + "、"

    participate_company_str = participate_company_str[:-1]

    
    df_output_part = pd.DataFrame([st_id.text, st_name.text, participate_company_str]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, st_name, participate_company, participate_company_str
    
   
    
    









