# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 11:01:31 2016

@author: anushila
"""

import pandas as pd
import pandas.io.data as web
import numpy as np

#######################################################
#
#  Main program
#
#######################################################

if __name__ == "__main__":
    
    tickers = {'S&P500' : '^GSPC', 'Dow Jones': '^DJI', 'NASDAQ' : '^IXIC', \
    'Russell 2000': '^RUT', 'Russell 3000': '^RUA'}
    
    
    
    #tickers = {'S&P500' : '^GSPC'}
    
    cash_months = [5, 6, 7, 8, 9, 10]
    #cash_months = [6, 7, 8]
    #df.ix[df.index.to_series().dt.month.isin(real_estate_hold_months), 'seasonal_ret'] = df['real_estate_ret']
    
#        lbmDates = pd.bdate_range('12/20/1988', periods=324, freq='BM')
#    june_returns = {}
    for key in tickers:
        
        ticker = tickers[key]       
        main_df = pd.DataFrame()
    
        df = web.DataReader(ticker, data_source='yahoo',start='12/30/1989', end='12/31/2015')
        #print df[df['Adj Close'].isnull()]
        #df = df.reindex(lbmDates)

    #print df['Adj Close'].head(30)
        main_df['Market'] = 1.0*np.log(df['Adj Close']/df['Adj Close'].shift(1))
        #print returns
#        df.ix[df.index.to_series().dt.month.isin(real_estate_hold_months), 'seasonal_ret'] = df['real_estate_ret']        
        # sp500['Regime'] = np.where(sp500['st-lt'] > sd, 1, 0)        
        #returns.ix[returns.index.to_series().dt.month.isin(may_to_oct), 'Strategy'] = 0
        #returns['Strategy'] = np.where(sp500['st-lt'] > sd, 1, 0)
        #returns.ix[returns.ix[returns.index.to_series().dt.month.isin(may_to_oct), 'Strategy'] = 0
                
        main_df['Strategy'] = main_df['Market']
        main_df['Strategy'][main_df.index.to_series().dt.month.isin(cash_months)] = 0
        main_df = main_df
        ax = (1000*main_df[['Market', 'Strategy']].cumsum().apply(np.exp)).plot(grid=True, \
                                    figsize=(8, 5), title=key)
        fig = ax.get_figure()
        #print cumRet[-1]
        fig.savefig(key)
        #returns.apply(np.exp())
        #main_df[ticker]    
