from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#%%

st_list = ["00935", "00944", "00960", "00971", "00972", "00980A", "00985A", "009812", "00987B", "00999A"]

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()



st_list = []

for i in range(1, 35):
    
    driver.get("https://www.ctbcinvestments.com.tw/Etf/List")
    
    time.sleep(1)
    
    st_url_id = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div[2]/section[2]/div/table/tbody/tr[' + str(i) + ']/td[2]/a')
    st_url_id.click()
    
    time.sleep(1)
    
    st_list.append(driver.current_url)
    
    
df_output = pd.DataFrame()

for i in st_list:
    
    driver.get(i)
    
    time.sleep(3)
    
    st_id = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[2]/div/section[2]/ul/li[20]')
    st_name = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[1]/h1')
    
    participate_company = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[2]/div/section[5]/table')
    participate_company = participate_company.text.split("\n")
    participate_company = participate_company[2:]
    
    participate_company_str = ""
    
    for j in participate_company:
        
        if(j.find("公司") != -1):
            
           participate_company_str = participate_company_str + j + "、"
    
    participate_company_str = participate_company_str[:-1]
    
    df_output_part = pd.DataFrame([st_id.text, st_name.text.split(" ")[1], participate_company_str]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, st_name, participate_company, participate_company_str
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
