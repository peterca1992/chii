import pandas as pd
import numpy as np
import yfinance as yf
from selenium import webdriver
from selenium.webdriver.common.by import By

#%%

df = yf.download("2408.TW", start = "2010-01-01", end = "2026-12-31", auto_adjust = True)

df.columns = ["close", "high", "low", "open", "volume"]
df = df.reset_index(drop = False)

df_tw = yf.download("^TWII", start = "2010-01-01", end = "2026-12-31", auto_adjust = True)

df_tw.columns = ["close", "high", "low", "open", "volume"]
df_tw  = df_tw.reset_index(drop = False)


#%%
#資料處理
#df_st_ret = pd.DataFrame(df["Date"].iloc[1:]).reset_index(drop = True)
#df_st_ret["st_ret"] = df["close"].iloc[1:].reset_index(drop = True) / df["close"].iloc[:-1].reset_index(drop = True) - 1

#df_tw_ret = pd.DataFrame(df_tw["Date"].iloc[1:]).reset_index(drop = True)
#df_tw_ret["tw_ret"] = df_tw["close"].iloc[1:].reset_index(drop = True) / df_tw["close"].iloc[:-1].reset_index(drop = True) - 1

#df_rs = pd.merge(df_st_ret, df_tw_ret, how = "left", on = "Date")
#df_rs["RS"] = df_rs["st_ret"] - df_rs["tw_ret"]

df_rs = pd.DataFrame(df["Date"])

df_rs = pd.merge(df_rs, df_tw[["Date", "close"]], how = "left", on = "Date")
df_rs = df_rs.rename(columns = {"close" : "tw"})

df_rs = pd.merge(df_rs, df[["Date", "close"]], how = "left", on = "Date")
df_rs = df_rs.rename(columns = {"close" : "st"})

for i in df_rs.columns[1:]:
    
    df_rs[i] = df_rs[i].fillna(method = "ffill")
    
del i

df_rs["RS"] = df_rs["st"] / df_rs["tw"]

df_rs['RS_MA20'] = df_rs['RS'].rolling(20).mean()
df_rs['tw_MA20'] = df_rs['tw'].rolling(20).mean()
df_rs['st_MA20'] = df_rs['st'].rolling(20).mean()

del df, df_tw

#%%
#找出標準差 建立強弱勢部位用的pos
df_rs2 = df_rs.dropna().reset_index(drop = True)

#產出月線的標準差
#step 1 產大盤的標準差再產出四個區間 建立大盤比例


set_std_daily = 22
tw_std = [np.NAN] * (set_std_daily - 1)
st_std = [np.NAN] * (set_std_daily - 1)

for i in range(set_std_daily, len(df_rs2) + 1):
    
    tw_std_list = df_rs2["tw_MA20"].iloc[(i-set_std_daily):i]
    tw_std.append(tw_std_list.std())
    

df_rs2["tw_std"] = tw_std

df_rs2["tw_MA20_2std"] = df_rs2["tw_MA20"] + 2 * df_rs2["tw_std"] 
df_rs2["tw_MA20_1std"] = df_rs2["tw_MA20"] + 1 * df_rs2["tw_std"]
df_rs2["tw_MA20_n1std"] = df_rs2["tw_MA20"] - 1 * df_rs2["tw_std"]
df_rs2["tw_MA20_n2std"] = df_rs2["tw_MA20"] - 2 * df_rs2["tw_std"]





#%%
#pos
def get_gamma(row):
    
    market_bull = row['tw'] > row['tw_MA20']
    stock_strong = row['RS'] > row['RS_MA20']
    
    #大盤強 個股強
    if market_bull and stock_strong:
        return 0.5
    
    #大盤不強 個股強
    elif not market_bull and stock_strong:
        return 1
    
    #大盤強 個股弱
    elif market_bull and not stock_strong:
        return 0.8
    
    else:
        return 1.2  
    


def get_gamma2(row):
    
    market_bull = row['tw'] > row['tw_MA20'] #大盤強
    stock_strong = row['RS'] > row['RS_MA20'] #股票強
    
    #大盤強 個股強
    if market_bull and stock_strong:
        
        market_pos = 0.25
        stock_pos = 1.2
        
        return market_pos, stock_pos
    
    #大盤不強 個股強
    elif not market_bull and stock_strong:
        
        market_pos = 0.75
        stock_pos = 1.2
        
        return market_pos, stock_pos
    
    #大盤強 個股弱
    elif market_bull and not stock_strong:
        
        market_pos = 0.25
        stock_pos = 0.25
        
        return market_pos, stock_pos
    
    else:
        return 1.2  
    
#%%
    
df_rs['pos'] = df_rs.apply(get_gamma, axis = 1)

df_rs2 = df_rs.dropna().reset_index(drop = True)

pos_ret = df_rs2["st_ret"].iloc[1:].reset_index(drop = True) - df_rs2["tw_ret"].iloc[1:].reset_index(drop = True) * df_rs2["pos"].iloc[:-1].reset_index(drop = True)














