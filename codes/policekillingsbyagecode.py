#This code gets numbers of police killings by age
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/baileykoo/Documents/BLM/police_killings.csv")
#df.dropna(inplace=True)
#df["Victim's age"]=df["Victim's age"].astype(int)

df["Victim's age"] = pd.to_numeric(df["Victim's age"], errors = "coerce")
df["Victim's age_freq"]=np.where(df["Victim's age"]<18,'<18',np.where(df["Victim's age"]<50,'<50',
                                                                    np.where(df["Victim's age"]<70,'<70',
                                                                    np.where(df["Victim's age"]<110,'<110',"x"))))
df["age"] = df["Victim's age_freq"][df["Victim's age_freq"] != 'x']

df["age"].dropna(inplace=True)

we=df.groupby(["age"]).count()

we.to_csv(r'/Users/baileykoo/Documents/agekillings.csv')
