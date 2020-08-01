
#PolicekilledVSPoliticalElection Outcome
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")
df_winning=pd.read_csv("/Users/baileykoo/Documents/politicElection.csv")





state_sum=df.groupby(['State']).count()

fig = plt.figure(figsize=(12,5))

plt.xticks(size=7)
plt.ylabel('Number of victims',size=10)
plt.title('Number of Victims by State')


#print(state_sum)
police_killing_total=df[["Victim's name", 'State']]
murder_state_total=police_killing_total.groupby('State')["Victim's name"].nunique()
murder_total_df=murder_state_total.to_frame()
#murder_total_df=pd.merge(murder_total_df, state, on='State')
plt.xlabel('State', size=10)
plt.ylabel('Number of death',size=10)
plt.title("graph")
plt.xticks(size=7)



ax=fig.add_subplot(111)

murder_state_total.plot.bar(label="Number of Victims",position=0,ax=ax,color='g',width=0.4,edgecolor='black')

ax2=ax.twinx()

df_police=pd.read_csv("/Users/baileykoo/Documents/BLM/police_deaths_538.csv")
death_sum = df_police.groupby(['state']).count()

police_killed_total2=df_police[["person","state"]]

murder_state_total2=police_killed_total2.groupby('state')["person"].nunique()

murder_state_total2.plot.bar(label="Number of police", position=1,ax=ax2,color='r',width=0.4,edgecolor='black')
fig.legend(loc="upper right")

plt.show()
