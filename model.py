import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import  adfuller #adf check
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
# 读取数据
df=pd.read_csv("D:\代码\新建文件夹\\2000.csv")
compare=pd.read_csv("D:\代码\新建文件夹\\2001.csv")
df.dtypes
df.head()
print(df.dtypes)
print(compare.dtypes)
#print(df)
train=df[["date","score"]]
compare_data=compare[["date","score"]]
print(train)
print(compare_data)
#train=df[:,20]
#print(train)
#print(sns.__version__)
#sns.set(style="ticks",context="poster")
#sns.relplot(x="date",y="score",data=train)

#plt.show()

# 移动平均图
def draw_trend(train, size=12):
    f=plt.figure(facecolor="white")
    #对size个数据进行移动平均 frage 什么叫做移动平均 什么叫size个数据
    rol_mean = train.rolling(window=size).mean()
    #什么叫做 加权移动平均 对size个数据进行加权移动平均
    rol_weighted_mean = pd.ewma(train, span=size)
    # ggplot 什么是ggplot 作用是什么
    import matplotlib
    matplotlib.style.use("ggplot")

    train.plot(color="blue", label="原始数据")
    rol_mean.plot(color="red", label="移动平均")
    rol_weighted_mean(color="black", label="加权移动平均")
    plt.legend(loc="best") #这一步的意思是什么
    plt.title("Rolling Mean")
    plt.show()

def testStarionarity(train): #acf 平稳性检验
    dftest = adfuller(train)

    dfoutput = pd.Series(dftest[0:4], index=["Test statistic","P","#Lags used","number of observations Used"])

    for key, value in dftest in dftest[4].items():
        dfoutput["critical Value(%s)" % key] = value
    return dfoutput

def draw_acf_pacf(train):

    f = plt.figure(facecolor="white")
    ax1=f.add_subplot(211)
    plot_acf(train, lags=40, ax=ax1)
    ax2= f.add_subplot(212)
    plot_pacf(train, lags=40, ax=ax2)
    plt.show()

def diff(train):

    fig = plt.figure(facecolor="white", figsize=(12,8))

    ax1=fig.add_subplot(221)
    date=train
    date_plot=date.plot()
    #一阶差分
    ax2=fig.add_subplot(222)
    diff_1=train.diff(1)
    date_diff_1_plot=diff_1.plot()
    #二阶差分
    ax3= fig.add_subplot(223)
    diff_2=train.diff(2)
    date_diff_2_plot=diff_2.plot()
    #三阶差分
    ax4 = fig.add_subplot(224)
    diff_3 = train.diff(3)
    date_diff_3_plot = diff_3.plot()
    plt.show()

    return  diff_1,diff_2,diff_3

def tsStationarity(diff_1):
    dftest = adfuller(diff_1)
    dfoutput=pd.Series(dftest[0:4], index=["Test Statistic", "p-value","#Lags Used","Number of Observations Used"])
    for key, value in dftest[4].items():
        dfoutput["critical Value(%s)" % key] = value
    return dfoutput

#确定 p跟d的阶数 '对于个数不多的时序数据，我们可以通过观察自相关图和偏相关图来进行模型识别.对于数量较多的时序数据，依据BIC准则识别模型的p, q值，通常认为BIC值越小的模型相对更优。BIC准则，它综合考虑了残差大小和自变量的个数，残差越小BIC值越小，自变量个数越多BIC值越大'
