import pandas as pd

df = pd.read_csv("/Users/YKim/Documents/Datamining/BLM/shootings_wash_post.csv")

state_sum = df.groupby(['state']).count()

df['date'] = pd.to_datetime(df['date'])
df['year'] = pd.to_datetime(df['date']).dt.year

df = df[df['year']==2016]
police_killing_total = df[["name", "state"]]
murder_state_total = police_killing_total.groupby('state')["name"].nunique()
murder_total_df = murder_state_total.to_frame()

murder_total_df.to_csv('/Users/YKim/Documents/Datamining/BLM/police_shooting_2016.csv')
