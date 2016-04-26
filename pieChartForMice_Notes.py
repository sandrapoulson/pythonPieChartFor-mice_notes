import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Some data

labels = 'Allogrooming', 'Rearing/Climbing', 'Burrowing', 'Grooming', 'Fluffing own nest', 'Other', 'Digging near mouse', 'Side-by-Side', 'Nesting'
#second 'Burrowing',  last , 'Nesting'
fracs = [48.6, 1.1, 0.5, 1.4, 0.2, 14.4, 1.5, 6.5, 25.9]
colors = ["#0000E6", "#FF0000", "#FF6666", "#FF8000", "#FFCC00", "#A6A6A6", "#00CC44", "#6A5ACD", "#00B3B3"]
#burrowing  "#FF6666", Digging near mouse "#00CC44", fluffing own nest "#FFCC00", digging near mouse "#00CC44", nesting , "#00B3B3"

plt.pie(fracs, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True)


plt.axis('equal')

plt.show()
