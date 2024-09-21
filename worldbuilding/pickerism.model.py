import csv
import math
import matplotlib.pyplot as plt
import numpy as np

# Preliminary population model



'''
# Calculations in pickerism.md

gamma = 7.798 * 10**30 # Picker time factor
init_picker_time = 3.1536 * 10**11 # Absolute Picker time / death
init_death_rate =  2.473 * 10**19 # Deaths / second

def d_picker_time(t): # Change in absolute Picker time / second
    return 


np.cumsum(d_picker_time(year_to_seconds*t))

t = np.linspace(0,1000,1000) # Years
year_to_seconds = 60*60*24*365
billion = 1000000000

d_death_rate = -gamma*(d_picker_time/(
    (xxx+init_picker_time)**2))

init_death_rate_billions =  init_death_rate/billion
d_death_rate_billions = d_death_rate/billion

death_rate_billions = np.cumsum(d_death_rate_billions)+init_death_rate_billions

picker_time_years = (d_picker_time*billion*sec_to_yr*t + init_picker_time)/billion*sec_to_yr

# Plotting

red = 'tab:red'
blue = 'tab:blue'

fig, ax1 = plt.subplots()
ax1.plot(t, d_death_rate_billions)

fig.suptitle("End of the Transcendentalists' War")

ax1.set_xlabel('Billions of Years')
ax1.set_ylabel('Death Rate (billions/s)', color=red)
ax1.tick_params(axis='y', labelcolor=red)
ax1.plot(t, death_rate_billions, color=red)

ax2 = ax1.twinx()

ax2.set_ylabel('Absolute Picker Time (years)', color=blue)
ax2.tick_params(axis='y', labelcolor=blue)
ax2.plot(t, picker_time_years, color=blue)

fig.tight_layout()
plt.show()
'''
