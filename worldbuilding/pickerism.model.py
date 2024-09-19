import csv
import math
import matplotlib.pyplot as plt
import numpy as np

# Grabs death data

data = []

with open('groups.pickerism.model.data.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append([int(row[0]), int(row[1])])

data = np.array(data)
years = data[:,0]
deaths_per_year = data[:,1]
years_per_death = 1./deaths_per_year

megadeaths_per_year = deaths_per_year/1000000
total_megadeaths = np.cumsum(megadeaths_per_year)

miliseconds_per_year = 365 * 24 * 60 * 60 * 1000
miliseconds_per_death = miliseconds_per_year * years_per_death

# An example plot, ignoring all sentient deaths not from Earth, gamma_p, and the
# Harolds' Time, showing the "calculus" behind Pickerism

red = 'tab:red'
blue = 'tab:blue'

fig1, ax1 = plt.subplots()
fig1.suptitle('Relative Picker Time vs Year (ignoring alien deaths)')

ax1.set_xlabel('Year')
ax1.set_ylabel('Total Megadeaths', color=red)
ax1.tick_params(axis='y', labelcolor=red)
ax1.plot(years, total_megadeaths, color=red)

ax2 = ax1.twinx()

ax2.set_ylabel('Relative Picker time (ms)', color=blue)
ax2.tick_params(axis='y', labelcolor=blue)
ax2.plot(years, miliseconds_per_death, color=blue)

fig1.tight_layout()
plt.show()
