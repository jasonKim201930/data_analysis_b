#racegroupkilledbystates2015/2016

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")
state_sum = df.groupby(['State']).count()
df['Date of Incident (month/day/year)'] = pd.to_datetime(df['Date of Incident (month/day/year)'])
df['year'] = pd.to_datetime(df['Date of Incident (month/day/year)']).dt.year
df = df[df['year']==2019]
police_killing_total = df[["Victim's name", "State"]]
murder_state_total = police_killing_total.groupby('State')["Victim's name"].nunique()
murder_total_df = murder_state_total.to_frame()

murder_total_df.to_csv('/Users/baileykoo/Documents/BLM/2019.csv')

df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")
state_sum = df.groupby(['State']).count()
df['Date of Incident (month/day/year)'] = pd.to_datetime(df['Date of Incident (month/day/year)'])
df['year'] = pd.to_datetime(df['Date of Incident (month/day/year)']).dt.year
df = df[df['year']==2020]
police_killing_total = df[["Victim's name", "State"]]
murder_state_total = police_killing_total.groupby('State')["Victim's name"].nunique()
murder_total_df2 = murder_state_total.to_frame()

murder_total_df2.to_csv('/Users/baileykoo/Documents/BLM/2020.csv')
