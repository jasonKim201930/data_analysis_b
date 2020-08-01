#This code draws a pi graph of Police Killings in California in respect to raceial groups present in data
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")
#df.dropna(inplace=True)
df["Victim's race"] = df["Victim's race"].str.replace("Unknown race","Unknown Race")
#df["Victim's race"] = df["Victim's race"].str.split(',').str[1].str.strip()
people=df[df["State"]=="CA"]
new_people=people[["Victim's name","Victim's race"]]
people_killed=new_people.groupby(["Victim's race"]).count()

#people_killed[people_killed["Victim's race"]=="Unkown Race"] = people_killed[people_killed["Victim's race"]=="Unkown Race"].str.replace(people_killed["Victim's race"]=="Unkown Race","")


killing=people_killed["Victim's name"].index
labels=killing
sizes=people_killed["Victim's name"]
explode=(0,0,0,0,0,0,0)


fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%', startangle=150,textprops={'fontsize':6.5},pctdistance=1.1,labeldistance=1.2)
ax1.axis('equal')
ax1.set_title('Police Killings by Race',pad=20)
fig1.show()

fig1.savefig("pie1.jpg")
