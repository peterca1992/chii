import pandas as pd


df_output = pd.DataFrame()
st_list = ["00703", "00734B", "00842B", "00851", "00936", "00942B", "00947", "00951", "00962", "00980B", "009806", "009807", "00986A", "00970B", "00987A", "00989B", "009805", "00904", "00775B", "00844B", "00867B"]

for i in st_list:
    
    df_infor = pd.read_html("https://www.tsit.com.tw/ETF/Home/ETFSeriesDetail/" + i)
    
    st_id = df_infor[0][df_infor[0][0] == "股票代號"][1].iloc[0]
    st_name = df_infor[0][df_infor[0][0] == "ETF 簡稱"][1].iloc[0]
    
    participate_company = df_infor[4]
    
    participate_company_str = ""
    
    for j in participate_company[0]:
        
        participate_company_str = participate_company_str + j + "、"
        
    participate_company_str = participate_company_str[:-1]
    
    df_output_part = pd.DataFrame([st_id, st_name, participate_company_str]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)

    del st_id, st_name, participate_company