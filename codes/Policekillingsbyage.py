#Policekillings by age
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

df =pd.read_csv("/Users/baileykoo/Documents/BLM/shootings_wash_post.csv")

df['date']=pd.to_datetime(df['date'])
df['year']=pd.to_datetime(df['date'])
#print(df['Date of Incident (month/day/year)'])
#df['year']=pd.to_datetime(df['Date of Incident (month/day/year)']).dt.year
df['month']=pd.to_datetime(df['date']).dt.month
df['month_n']=df['date'].dt.strftime('%B')
df['month_num']=df['date'].dt.strftime('%n')
df['week']=df['date'].dt.strftime('%A')
#df['date_num']=df['Date of Incident (month/day/year)'].dt.strftime('%d').astype(int)
#df['date_separate']=np.where(df['date_num']>16,"First half", "Second half")
df['date_mon']=df['date'].dt.to_period("M")
df.dropna(inplace=True)
df["age"] = df["age"].astype(int)
print(df["age"])
df["Victim's age_freq"]=np.where(df["age"]<18,'<18',np.where(df["age"]<30,'<30',np.where(df["age"]<40,'<40',np.where(df["age"]<50,'<50',np.where(df["age"]<60,'<60', np.where(df["age"]<70,'<70',
                                                                np.where(df["age"]<80,'<80',np.where(df["age"]<90,'<90',np.where(df["age"]<100,'<100', np.where(df["age"]<110,'<110',"x"))))))))))

df['date']=pd.to_datetime(df['date'])

monthly_df=df['date'].groupby(df.date.dt.to_period("M")).agg('count').to_frame(name="count").reset_index()
year=[]

print("monthly_df")
for i in monthly_df['date']:
    year.append(str(i))
monthly_df.plot.bar(x="date",y="count")
fig=plt.figure(figsize=(12,5))
ax=fig.gca()

plt.show()
print(year)

print(type(monthly_df))
print(df["age"])
print(df["Victim's age_freq"])
#print(df['year'])
#print(df['month'])
#print(df['month_n'])
