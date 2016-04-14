import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Some data

labels = 'Allogrooming', 'Burrowing', 'Rearing/Climbing', 'Grooming', 'Other', 'Side-by-Side', 'Nesting'
#second 'Burrowing',  last , 'Nesting'
fracs = [16.5, 42.8, 1.1, 1.6, 28.3, 2.0, 7.8]
colors = ["#0000E6", "#FF0000", "#FF6666", "#FF8000", "#A6A6A6", "#6A5ACD", "#00B3B3"]
#burrowing "#FF0000",  nesting , "#00B3B3"

plt.pie(fracs, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True)


plt.axis('equal')

plt.show()
