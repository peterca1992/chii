from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()


st_list = ["009802", "00900", "00892", "009809", "00733", "00730", "00692", "006208", "0057", "0052", "00717", "00885", "006205", "00639", "00783", "00700", "00645", "00652", "00920", "00908", "00903", "00879", "00895", "00662", "00709", "009814", "00675L", "00676R", "00633L", "00634R", "00665L", "00666R", "00640L", "00641R", "00653L", "00654R", "00670L", "00671R", "00694B", "00695B", "00696B", "00845B", "00746B", "00740B", "00741B", "00846B", "00785B", "00982D", "00983D"]

df_output = pd.DataFrame()

for i in st_list:
   
    driver.get("https://websys.fsit.com.tw/FubonETF/Fund/Participating.aspx?stkId=" + i)
    
    time.sleep(2)
    
    
    participate_company = driver.find_element(By.XPATH, '//*[@id="form1"]/article/div/div/div/ul[2]')
    

    participate_company_str = ""
    
    for j in participate_company.text.split("\n"):
        
        if(j.find("股份有限公司") != -1):
            participate_company_str = participate_company_str + j + "、"

    
    participate_company_str = participate_company_str[:-1]

    
    st_id = driver.find_element(By.XPATH, '//*[@id="mainContent_Panel2"]/h5')  
    

    df_output_part = pd.DataFrame([st_id.text.split("\n")[0].split(" / ")[0], st_id.text.split("\n")[0].split(" / ")[1], participate_company_str]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, participate_company, participate_company_str
    
    
    
     
     
     
     
     
     
     
     