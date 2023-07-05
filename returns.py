#functions to calculate returns
import numpy as np

def daily_returns(df):
    df_daily_return = df.copy()
    for i in df_daily_return.columns[1:]:
        for j in range(1,len(df)):
            df_daily_return[i][j] = ((df[i][j] -df[i][j-1])/df[i][j-1])*100
        df_daily_return[i][0] = 0
    return df_daily_return

def beta(stocks_daily_return,stock):
    market_return = stocks_daily_return["sp500"].mean()*252  #252 is the number of active trading days
    b,a = np.polyfit(stocks_daily_return['sp500'],stocks_daily_return[stock],1)
    return b,a