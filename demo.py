#policekillings divided by demographic 2018 and 2019
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")




df['Date of Incident (month/day/year)'] = pd.to_datetime(df['Date of Incident (month/day/year)'])
df['year'] = pd.to_datetime(df['Date of Incident (month/day/year)']).dt.year
df = df[df['year'].isin([2018,2019])]
df2 = df[df["Victim's race"]=='Hispanic']

police_killing_total=df2[["Victim's name", 'State']]
murder_state_total=police_killing_total.groupby('State')["Victim's name"].nunique()

my_data2=pd.read_csv("/Users/baileykoo/Desktop/Datascienceresearch/OriginalData/Demographicstate.csv")
my_data2 = my_data2.set_index('State')
my_data2 = my_data2.rename(columns = {'Hispanic (of any race)' : 'Hispanic', 'Non-Hispanic White' : 'White', 'Non-Hispanic Black' : 'Black', 'Non-Hispanic Asian' : 'Asian', 'Non-Hispanic American Indian' : 'Native American'})
my_data2 = my_data2.sort_index()

new_data = pd.merge(murder_state_total, my_data2,on='State')
new_data["prob_hispanic"] = new_data["Victim's name"]/new_data["Hispanic"]*100000


df3 = df[df["Victim's race"]=='White']
police_killing_total3=df2[["Victim's name", 'State']]
murder_state_total3=police_killing_total3.groupby('State')["Victim's name"].nunique()

my_data3=pd.read_csv("/Users/baileykoo/Desktop/Datascienceresearch/OriginalData/Demographicstate.csv")
my_data3 = my_data3.set_index('State')
my_data3 = my_data3.rename(columns = {'Hispanic (of any race)' : 'Hispanic', 'Non-Hispanic White' : 'White', 'Non-Hispanic Black' : 'Black', 'Non-Hispanic Asian' : 'Asian', 'Non-Hispanic American Indian' : 'Native American'})
my_data3 = my_data3.sort_index()

new_data3 = pd.merge(murder_state_total3, my_data3,on='State')
new_data["prob_white"] = new_data3["Victim's name"]/new_data3["White"]*100000

df4 = df[df["Victim's race"]=='Black']
police_killing_total4=df2[["Victim's name", 'State']]
murder_state_total4=police_killing_total4.groupby('State')["Victim's name"].nunique()

my_data4=pd.read_csv("/Users/baileykoo/Desktop/Datascienceresearch/OriginalData/Demographicstate.csv")
my_data4 = my_data4.set_index('State')
my_data4 = my_data4.rename(columns = {'Hispanic (of any race)' : 'Hispanic', 'Non-Hispanic White' : 'White', 'Non-Hispanic Black' : 'Black', 'Non-Hispanic Asian' : 'Asian', 'Non-Hispanic American Indian' : 'Native American'})
my_data4 = my_data4.sort_index()

new_data4 = pd.merge(murder_state_total4, my_data4,on='State')
new_data["prob_black"] = new_data4["Victim's name"]/new_data4["Black"]*100000

df5 = df[df["Victim's race"]=='Asian']
police_killing_total5=df2[["Victim's name", 'State']]
murder_state_total5=police_killing_total5.groupby('State')["Victim's name"].nunique()

my_data5=pd.read_csv("/Users/baileykoo/Desktop/Datascienceresearch/OriginalData/Demographicstate.csv")
my_data5 = my_data5.set_index('State')
my_data5 = my_data5.rename(columns = {'Hispanic (of any race)' : 'Hispanic', 'Non-Hispanic White' : 'White', 'Non-Hispanic Black' : 'Black', 'Non-Hispanic Asian' : 'Asian', 'Non-Hispanic American Indian' : 'Native American'})
my_data5 = my_data5.sort_index()

new_data5 = pd.merge(murder_state_total5, my_data2,on='State')
new_data["prob_asian"] = new_data5["Victim's name"]/new_data5["Asian"]*100000


new_data.to_csv("/Users/baileykoo/Desktop/Datascienceresearch/Demographicrace201819.csv")
