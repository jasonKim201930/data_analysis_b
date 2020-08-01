#Indiana police killings by race
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")

df["Victim's race"] = df["Victim's race"].str.replace("Unknown race","Unknown Race")

people=df[df["State"]=="IN"]
new_people=people[["Victim's name","Victim's race"]]
people_killed=new_people.groupby(["Victim's race"]).count()

#people_killed[people_killed["Victim's race"]=="Unkown Race"] = people_killed[people_killed["Victim's race"]=="Unkown Race"].str.replace(people_killed["Victim's race"]=="Unkown Race","")
print(people_killed)

killing=people_killed["Victim's name"].index
labels=killing
sizes=people_killed["Victim's name"]
explode=(0,0,0,0)


fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%', startangle=150,textprops={'fontsize':10},pctdistance=1.1,labeldistance=1.2)
ax1.axis('equal')
ax1.set_title('Police Killings by Race (IN)',pad=30)
fig1.show()

fig1.savefig("INkilled_fixxxx.jpg")
