import pandas as pd

df = pd.read_csv("/Users/YKim/Documents/Datamining/BLM/police_killings.csv")


#df["Criminal Charges?"] = df["Criminal Charges?"].str[0].str.strip()

victims_total = df[["Unarmed","Victim's name"]]

armed_total = victims_total.groupby("Unarmed")["Victim's name"].nunique()
print(armed_total)
