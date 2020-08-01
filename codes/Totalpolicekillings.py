#Total police killings by race groups
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")

#fig = plt.figure(figsize=(12,5))

#plt.xticks(size=7)
#plt.ylabel('Number of victims',size=10)
#plt.title('Number of Victims by State')

#ax=fig.add_subplot(111)

w=df[df["Victim's race"]=="White"]
new_w=w[["Victim's name","State"]]
white_killed=new_w.groupby(['State']).count()
#ax=fig.add_subplot(111)
#white_killed.plot.bar(label="White",position=0,ax=ax,color='r',width=0.3,edgecolor='black')


#ax2=ax.twinx()
b=df[df["Victim's race"]=="Black"]
new_b=b[["Victim's name","State"]]
black_killed=new_b.groupby(['State']).count()
#black_killed.plot.bar(label="Black",position=1,color='g',ax=ax2,width=0.3,edgecolor='black')


#ax3=ax.twinx()
h=df[df["Victim's race"]=="Hispanic"]
new_h=h[["Victim's name","State"]]
hispanic_killed=new_h.groupby(['State']).count()
#hispanic_killed.plot.bar(label="Hispanic",position=2,color='b',ax=ax3,width=0.3,edgecolor='black')


#ax4=ax.twinx()
p=df[df["Victim's race"]=="Pacific Islander"]
new_p=p[["Victim's name","State"]]
pacificislander_killed=new_p.groupby(['State']).count()
#pacificislander_killed.plot.bar(label="Pacific Islander",position=3,color='y',ax=ax4,width=0.3,edgecolor='black')


#ax5=ax.twinx()
a=df[df["Victim's race"]=="Asian"]
new_a=a[["Victim's name","State"]]
asian_killed=new_a.groupby(['State']).count()
#asian_killed.plot.bar(label="Asian",position=4,color='#F885CE',ax=ax5,width=0.3,edgecolor='black')


#ax6=ax.twinx()
u=df[df["Victim's race"]=="Unknown race"]
new_u=u[["Victim's name","State"]]
unknown_killed=new_u.groupby(['State']).count()
#unknown_killed.plot.bar(label="Unknown",position=5,color='#F9AF10',ax=ax3,width=0.3,edgecolor='black')

print(white_killed,unknown_killed)

#plt.show()
