import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#%%

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

st_list = pd.read_csv("D:\\Python_code\\工作內容\\2026\\0320_參與券商確認\\ST.csv")


#%%
st_list = ["E66", "E82", "E83", "E84", "E87", "E88", "E93", "E94", "EA8", "EDY", "EA9", "EAA", "EAD", "EAE", "EAJ", "EAK", "EAL", "EAW", "EAU", "EAV", "EBE", "EBH", "EBJ", "EBK", "EBI", "EBQ", "EBO", "EC2", "ECB", "ECC", "ECN", "ECR", "ECW", "ED6", "EDD", "EDF", "EDO", "EDT", "EE9"]
#eav

df_output = pd.DataFrame()

for i in st_list:
    
    url = "https://www.cathaysite.com.tw/ETF/detail/" + i
    
    driver.get(url)
    time.sleep(5)
    
    #下滾
    for k in range(1):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2) # 暫停等待內容加載
    
    participate_company_click = driver.find_element(By.XPATH, '//*[@id="basic_info"]/app-basic-info/div/div/div[3]/div/div[4]')
    participate_company_click.click()
    
    
    participate_company = driver.find_element(By.XPATH, '//*[@id="basic_info"]/app-basic-info/div/div/div[3]/div/div[5]/div/div[2]')

    
    participate_company = participate_company.text.split("\n")
    
    participate_company_str = ""
 
    for j in participate_company:
     
        if(j.split(" ")[0].find("股份有限公司") != -1):
            participate_company_str = participate_company_str + j.split(" ")[0] + "、"
 
    participate_company_str = participate_company_str[:-1]
    
    st_id = driver.find_element(By.XPATH, '/html/body/app-root/app-etf/app-etf-detail/app-banner/div[1]/div/div[2]/div[1]/div[2]/div[2]/h1')
    st_id.text
    
    df_output_part = pd.DataFrame([st_id.text.split(" ")[0], st_id.text.split(" ")[1], participate_company_str]).T
    
    df_output = pd.concat([df_output, df_output_part], axis = 0)


























