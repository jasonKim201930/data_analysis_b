import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/Users/YKim/Documents/Datamining/BLM/police_killings.csv")

state_sum = df.groupby(['State']).count()
fig = plt.figure(figsize=(12,5))

police_killing_total = df[["Victim's name", "State"]]
murder_state_total = police_killing_total.groupby('State')["Victim's name"].nunique()
murder_total_df = murder_state_total.to_frame()
murder_total_df = pd.merge(murder_total_df, murder_state_total, on='State')

plt.xlabel('State', size = 10)

plt.title("Cases of Police Deaths and Killings 2013-2019 by State")
plt.xticks(size = 7)

ax = fig.add_subplot(111)
ax.set_ylabel('Number of Victims Killed')
murder_state_total.plot.bar(label = "Victims",position=2,ax=ax, color='y', width=0.2, edgecolor='black')
ax2 = ax.twinx()

ax2.set_ylabel('Number of Police Killed')
df_police = df = pd.read_csv('/Users/YKim/Documents/Datamining/BLM/police_deaths_538.csv')

df_police['date'] = df_police['eow'].str.replace("EOW:","")
df_police['date'] = pd.to_datetime(df_police['date'])
df_police['year'] = pd.to_datetime(df_police['date']).dt.year

df_police = df_police[df_police['year']>=2013]
df_police = df_police[~df_police['state'].isin([' GU', ' PR', ' US', ' TR'])]

police_killed_total = df_police[["person", "state"]]
murder_state_total2 = police_killed_total.groupby('state')["person"].nunique()
murder_state_total2.plot.bar(label = "Police",position=1,ax=ax2, color='b', width=0.2, edgecolor='black')

fig.legend(loc = "upper left")

plt.show()
