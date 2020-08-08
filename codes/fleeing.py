import matplotlib.pyplot as plt

labels = 'Fled by Car', 'Fled by foot', 'Other','Not fled', 'Unknown'
sizes = [79400/7664,61800/7664,14000/7664,328100/7664,283100/7664]
explode = (0, 0, 0, 0.1, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')

plt.title("Percentage of Victims who fled during the encounter with the Police\n" + "2013-2019")
plt.show()

