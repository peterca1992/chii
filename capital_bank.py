from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#%%

st_list = ["195", "378", "389", "399", "500", "390", "365", "388", "366", "175", "069", "093", "094", "095", "102", "103", "104", "105", "171", "172", "173", "189", "190", "192", "193"]
, "502"


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

df_output = pd.DataFrame()

for i in st_list:
    
    driver.get("https://www.capitalfund.com.tw/etf/product/detail/" + i + "/supplier")
    
    time.sleep(1)
    
    st_id = driver.find_element(By.XPATH, '/html/body/app-root/layout-etf/main/app-etf/app-etf-product-detail/section[1]/div[2]/div/div/h1/b')
    participate_company = driver.find_element(By.XPATH, '/html/body/app-root/layout-etf/main/app-etf/app-etf-product-detail/section[4]/div/app-etf-product-detail-supplier/div/div/div[1]/div[2]')
    
    participate_company_str = ""

    for j in participate_company.text.split("\n"):
        
        if(j.split(" ")[0].find("證券") != -1):
            participate_company_str = participate_company_str + j.split(" ")[0] + "、"

    participate_company_str = participate_company_str[:-1]

    
    df_output_part = pd.DataFrame([st_id.text.split(" ")[0], st_id.text.split(" ")[1], participate_company_str]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, participate_company, participate_company_str
    
    
    
    









