import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
year_to_seconds = 60*60*24*365
billion = 1000000000
million = 1000000

## Preliminary population model ##

# Unused because of exp() computational limit
#def pop_model(P_init, K, r, t): # All inputs in seconds
#    top = P_init*K*math.exp(r*t)
#    bottom = (K-P_init) + P_init*math.exp(r*t)
#    return top/bottom

#v_pop_model = np.vectorize(pop_model, excluded=['P_init','K','r'])

# Population vs Time (No War)
r = 3.171 * 10**-10 # Rate of natural increase / sec
r_ma = 0.25#r*million*year_to_seconds # ... / Ma

pop_init = 10**10 # Initial population at t_init
civ_pop_init = 5#pop_init/(billion*10) # ... num civilizations

carry = 1.560*10**30 # Carrying capacity
civ_carry = 100#carry/(billion*10) # ... num civilizations

t_init = -5000 # Ma
t_end = 100 # Ma

t = np.arange(t_init,1,t_end)
pop = np.array([civ_pop_init])

for i in t:
    diff = r_ma*pop[-1]*(1 - pop[-1]/civ_carry)
    pop = np.append(pop,pop[-1]+diff)

pop = pop[0:-1] # pop goes 1 over size(t)

fig1, ax = plt.subplots()
fig1.suptitle("Population Model (No War)")

ax.plot(t,pop)
ax.set_title("Population vs Time")
ax.set_xlabel("Millions of Years")
ax.set_ylabel("Number of Civilizations")
plt.show()

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
