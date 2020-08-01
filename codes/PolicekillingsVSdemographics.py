#Arkansas policekillings divided by demographics

import pandas as pd
import matplotlib.pyplot as plt
file_path = '/Users/baileykoo/Documents/BLM/police_killings.csv'
my_data = pd.read_csv(file_path)
state_sum = my_data.groupby(['State', "Victim's race"]).count()
#print(state_sum["Victim's name"])
#print(state_sum)
​
race_AK = state_sum.loc['AK']["Victim's name"].index
#print(race_AK)
labels = race_AK
sizes = state_sum.loc['AK']["Victim's name"]
explode = (0.5, 0, 0, 0, 0, 0) 
​
#fig1, ax1 = plt.subplots()
#ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=150)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Police Killings as Percentage')
​
#fig1.show()
df = pd.read_csv('/Users/baileykoo/Documents/BLM/police_killings.csv')
#print(my_data.info())
​
​
missing = my_data.isna().sum()*100/my_data.shape[0]
#print(missing)
​
my_data.dropna(inplace=True)
​
my_data2 = pd.read_excel('C:/Users/CK\Downloads/697683_1307223_bundle_archive/Demographic_by_state.xlsx')
my_data2 = my_data2.set_index('State')
my_data2 = my_data2.rename(columns = {'Hispanic (of any race)' : 'Hispanic', 'Non-Hispanic White' : 'White', 'Non-Hispanic Black' : 'Black', 'Non-Hispanic Asian' : 'Asian', 'Non-Hispanic American Indian' : 'Native American'})
my_data2 = my_data2.sort_index()
#print(my_data2.head())
​
my_data.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
​
print(my_data.columns)
print(my_data["Victim's race"].values())
my_data["Victim's race"].unique()
#print(my_data["Victim's race"].unique())
hispanic_data = my_data[my_data["Victim's race"] == 'Hispanic']
​
sorted_hm = hispanic_data[["Victim's name", 'State']]
​
hispanic_group = sorted_hm.groupby('State')["Victim's name"].nunique()
​
hispanic_df = hispanic_group.to_frame()
hispanic_df = hispanic_df.rename(columns = {"Victim's name" : 'Hispanic Police Killings'})
hispanic_df.to_csv("C:/Users/CK\Downloads/697683_1307223_bundle_archive/test.csv")
Collapse




















