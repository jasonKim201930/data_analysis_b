import matplotlib.pyplot as plt

labels = 'Charged with a crime', 'No known charges'
sizes = [101/7413, 7312/7413]
explode = (0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')

plt.title("Percentage of Victims who had Criminal Charges\n" + "2013-2019")
plt.show()
