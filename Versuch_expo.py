from pandas import read_csv
from pandas import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing


#############################################################################################################################################

#Data

Data = pd.read_csv('C:/Users/Lena Engler/Desktop/Techlab/Neuer Ordner/2000-2002.csv',  index_col='date',parse_dates = True)


#############################################################################################################################

# Plot


df = pd.DataFrame(Data, columns = ['date', 'score'])
df_data = pd.DataFrame(Data)
plt.plot_date( df['date'],df['score'] , linestyle='-',markersize = '1.0')


plt.title('Score by day')
plt.xlabel('Date')
plt.ylabel('Score')
plt.tight_layout()
plt.xticks(np.arange(0, 1100, 98))

################################################################################################################################


train = df_data.loc['2000-01-04':'2000-12-31', :]

train_score = pd.DataFrame(train, columns = ['score'])

df_intpol = train_score.interpolate(method='time')
df_intpol.dropna(how='any', inplace=True)
np_train_score = df_intpol.values



df_smoothing = ExponentialSmoothing(np_train_score, trend='add', seasonal='add',seasonal_periods=7 ).fit(smoothing_level=0.2, optimized = False )

#out = pd.DataFrame(df_smoothing).set_index(train.index)

plt.df_smoothing()
plt.show()

##################################################################################################################################
