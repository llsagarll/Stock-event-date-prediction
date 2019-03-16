import csv
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('amd.us.txt')
df['close-open']=df['Close']-df['Open'].shift(1)
df['high-open']=df['High']-df['Open']
df['open-low']=df['Open']-df['Low']
p=df['close-open']
q=df['high-open']
s=df['open-low']
df['MAAX'] = df['Close']
pd.options.mode.chained_assignment = None  # default='warn'
for i in range(df['Close'].size):
    df['MAAX'].iloc[i] =max(df['close-open'].iloc[i] ,df['high-open'].iloc[i] , df['open-low'].iloc[i])
df['Date'] = pd.to_datetime(df['Date'])
i=0
df['Date'] = pd.to_datetime(df['Date']).dt.date
avg=df['MAAX'].mean()
maxx=df['MAAX'].max()
avg=(maxx-avg)/2.0
plt.figure(figsize=(30,6))
plt.plot(df['Date'] ,df['MAAX'])
plt.axhline(y=avg, color='r', linestyle='-')
plt.show()
df['Date'] = pd.to_datetime(df['Date']).dt.date
print(" *************************  Events happend on these dates : *****************************")
i=0
for i in range (df['MAAX'].size):
    if df['MAAX'].iloc[i]>avg:
        print (df['Date'].iloc[i])
