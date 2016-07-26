import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Some data

labels = 'Allogrooming', 'Rearing/Climbing', 'Burrowing', 'Pulling/Aggressive', 'Grooming', 'Fluffing own nest', 'Other', 'Digging near mouse', 'Side-by-Side', 'Nesting'
#order A, R, B, M, G, F, O, D, S, N
fracs = [30.0, 5.3, 1.1, 2.1, 3.7, 6.4, 35.2, 0.2, 14.2, 1.8]
colors = ["#0000E6", "#FF0000", "#FF6666", "#FF6633", "#FF8000", "#FFCC00", "#A6A6A6", "#00CC44", "#6A5ACD", "#00B3B3"]
# A"#0000E6", R"#FF0000", B"#FF6666", M "#FF6633", G"#FF8000", F"#FFCC00", O"#A6A6A6", D"#00CC44", S"#6A5ACD", N"#00B3B3"

plt.pie(fracs, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True, startangle=0)


plt.axis('equal')

plt.show()
