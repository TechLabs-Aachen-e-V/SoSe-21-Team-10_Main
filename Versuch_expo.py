from pandas import read_csv
from pandas import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.holtwinters import SimpleExpSmoothing


#############################################################################################################################################

#Data

Data = pd.read_csv('C:/Users/Lena Engler/Desktop/Techlab/Neuer Ordner/2000-2002.csv')


#############################################################################################################################

# Plot


df = pd.DataFrame(Data, columns = ['date', 'score'])

plt.plot_date( df['date'],df['score'] , linestyle='-',markersize = '1.0')


plt.title('Score by day')
plt.xlabel('Date')
plt.ylabel('Score')
plt.tight_layout()
plt.xticks(np.arange(0, 1100, 98))




################################################################################################################################

train = df.loc['2000-01-01':'2000-12-31', :]

df_smoothing = SimpleExpSmoothing(train).fit(smoothing_level=0.2, optimized = False )

out = pd.DataFrame(df_smoothing).set_index(train.index)

plt.out()

plt.show()




##################################################################################################################################
