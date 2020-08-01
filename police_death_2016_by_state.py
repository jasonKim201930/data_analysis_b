import pandas as pd

df = pd.read_csv("/Users/YKim/Documents/BLM/police_deaths_538.csv")

state_sum = df.groupby(['state']).count()

df = df[df['year']==2016]
police_killed_total = df[["person", "state"]]
murder_state_total = police_killed_total.groupby('state')["person"].nunique()
murder_total_df = murder_state_total.to_frame()

murder_total_df.to_csv('/Users/YKim/Documents/BLM/police_killed_2016.csv')
