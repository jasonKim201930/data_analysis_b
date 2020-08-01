import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/YKim/Documents/BLM/shootings_wash_post.csv')

fig = plt.figure(figsize=(12,5))
ax=fig.gca()

df['date'] = pd.to_datetime(df['date'])
df['year'] = pd.to_datetime(df['date']).dt.year

monthly = df['date'].groupby(df.date.dt.to_period("M")).agg('count').to_frame(name="count").reset_index()
monthly['year'] = monthly['date'].dt.strftime('%Y')

month = []
for i in monthly.loc[monthly['year'] == '2017']['date']:
                month.append(str(i))

plt.bar(month, monthly.loc[monthly['year'] == '2017']['count'], color='#5DADE2')

plt.xlabel('Month')
plt.ylabel('Number of death')
plt.title("Cases of Police Killing in 2017")

plt.show()
