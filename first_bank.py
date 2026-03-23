import pandas as pd


st_list = ["182", "177", "167", "101", "D90"]
df_output = pd.DataFrame()

for i in st_list:
    
    df_infor = pd.read_html("https://www.fsitc.com.tw/FundDetail.aspx?ID=" + i + "#TabLinkdivEditTab7")
    
    for j in range(0, len(df_infor)):
        
        df_infor_part = df_infor[j]
        
        if((df_infor_part.columns.to_list() == [0, 1]) and len(df_infor_part) > 1):
            
            if(len(df_infor_part[df_infor_part[0] == "股票代號"]) == 1):
                
                st_id = df_infor_part[df_infor_part[0] == "股票代號"][1].iloc[0]
                
            if(len(df_infor_part[df_infor_part[0] == "股票簡稱"]) == 1):
                
                st_name = df_infor_part[df_infor_part[0] == "股票簡稱"][1].iloc[0]
                
            if(len(df_infor_part[df_infor_part[0] == "ETF參與券商"]) == 1):
                
                participate_company = df_infor_part[df_infor_part[0] == "ETF參與券商"][1].iloc[0]


    df_output_part = pd.DataFrame([st_id, st_name, participate_company]).T
    df_output = pd.concat([df_output, df_output_part], axis = 0)
    
    del st_id, st_name, participate_company