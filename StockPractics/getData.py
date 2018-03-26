import tushare as ts
import pandas as pd

d = ts.get_tick_data('600887',date='2018-03-23')
print(d)
e = ts.get_hist_data('600887',start='2017-10-23',end='2018-03-26')
print(e)

e = ts.get_today_all()
print(e)
h5 = pd.HDFStore('data/tmp.h5','w')
h5['data'] = e
h5.close()