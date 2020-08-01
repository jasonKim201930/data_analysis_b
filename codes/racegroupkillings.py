#(racegroup)killings

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/baileykoo/Documents/Demographicstate.csv")
df_killings=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")

#Hispanic
state_sum=df.groupby(['State']).count()
hispanic_population=df[["Non-Hispanic Asian",'State']]

#df_killings=pd.read_csv("/Users/baileykoo/Documents/policekillings.py")
hispanic_killed=df_killings[df_killings["Victim's race"]=="Asian"]
h_killed=hispanic_killed.groupby(["State"]).count()
#print(h_killed)
new_df = pd.merge(hispanic_population,h_killed,on = 'State')

new_df["per"] = new_df["Victim's name"].astype(int) / new_df["Non-Hispanic Asian"].astype(int)

df=pd.read_csv("/Users/baileykoo/Documents/Demographicstate.csv")
df_killings=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")

#Black
df=pd.read_csv("/Users/baileykoo/Documents/Demographicstate.csv")
df_killings=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")
state_sum2=df.groupby(['State']).count()
black_population=df[["Non-Hispanic Asian",'State']]

#df_killings=pd.read_csv("/Users/baileykoo/Documents/policekillings.py")
hispanic_killed=df_killings[df_killings["Victim's race"]=="Asian"]
h_killed=hispanic_killed.groupby(["State"]).count()
#print(h_killed)
new_df = pd.merge(hispanic_population,h_killed,on = 'State')

new_df["per"] = new_df["Victim's name"].astype(int) / new_df["Non-Hispanic Asian"].astype(int)




print(new_df["per"])
new_df.to_csv(r'/Users/baileykoo/Documents/Asianfloatt.csv')

#new_df.to_csv("/Users/baileykoo/Documents/Demographicstate2.csv")




