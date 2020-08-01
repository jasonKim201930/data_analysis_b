#This code draws a pi graph in respect to Police's death by sate
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.xticks(size=7)
plt.yticks(size=12)
plt.title("Police death")
df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_deaths_538.csv")
#print(df.info())
death_sum = df.groupby(['state']).count()
#print(death_sum)
police_killed_total=df[["person","state"]]

murder_state_total=police_killed_total.groupby('state')["person"].nunique()
#print(police_killed_total)
murder_total_df=murder_state_total.to_frame()

murder_state_total.plot.bar(color='#FAFE97')
plt.show()
