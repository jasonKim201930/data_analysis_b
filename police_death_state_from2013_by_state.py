import pandas as pd
import matplotlib.pyplot as plt

df_police = df = pd.read_csv('/Users/YKim/Documents/BLM/police_deaths_538.csv')

df['eow'] = df['eow'].str.replace("EOW:","")
df['date'] = pd.to_datetime(df['eow'])
df['year'] = pd.to_datetime(df['date']).dt.year

df_police = df[df['year']>=2013]

police_killed_total = df_police[["person", "state"]]
murder_state_total = police_killed_total.groupby('state')["person"].nunique()

murder_state_total.plot.bar(color='r', width=0.4, edgecolor='black')

fig = plt.figure(figsize=(12,5))
plt.xlabel('State', size = 10)
plt.ylabel('Number of death')
plt.title("Cases of Police Death by State")
plt.xticks(size = 7)

ax = fig.add_subplot(111)

murder_state_total.to_csv('/Users/YKim/Documents/BLM/police_death_state.csv')

#plt.show()
