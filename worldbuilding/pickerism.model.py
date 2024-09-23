import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
year_to_seconds = 60*60*24*365
billion = 1000000000
million = 1000000

## Preliminary population model ##

def make_pop(r, pop_init, carry, t_init, t_end, iterator=1):
    '''
    Makes time/population data for a population model using logistic parameters.
    '''
    t = np.arange(t_init,t_end+1,iterator)
    pop = np.array([pop_init])
    d_pop = np.array([])

    for i in t:
        limiter = 1 - (pop[-1]/carry)
        diff = pop[-1]*r*limiter
        next_val = pop[-1]+diff
        if next_val > carry: # Protects against going beyond carry
            # This fills the rest before stopping for loop
            fill = np.ones(np.size(t) - np.size(pop) + 1)*carry
            pop = np.append(pop,fill)
            d_fill = np.zeros(np.size(t) - np.size(pop) + 1)
            d_pop = np.append(pop,d_fill)
            d_pop = d_pop[0:-1] # Hack, I have no idea why this works
            break
        pop = np.append(pop,pop[-1]+diff)
        d_pop = np.append(d_pop,diff)

    pop = pop[0:-1] # pop goes 1 over size(t)
    
    return t, pop, d_pop

# Population vs Time (No War)

pop_init = 10**10 # Initial population at t_init
carry = 1.560 * (10**30) # Carrying capacity

t_init = -5000 # Ma
t_end = 100 # Ma

# For individual-based model
r_1 = 3.171 * (10**-10) # Rate of natural increase / sec
r_ma_1 = r_1*million*year_to_seconds # ... / Ma

# For civilizational unit-based model
r_ma_2 = 0.02 # ... / Ma
civ_pop_init = pop_init/(billion*10) # ... num civilizations
civ_carry = carry/(billion*10) # ... num civilizations

t, pop1, d_pop1 = make_pop(r_ma_1, pop_init, carry, t_init, t_end)
t, pop2, d_pop2 = make_pop(r_ma_2, civ_pop_init, civ_carry, t_init, t_end)

fig1, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2)
fig1.suptitle("Population Model (No War)")

ax1.plot(t,pop1)
ax1.set_title("Pop vs T (r1)")
ax1.set_xlabel("Millions of Years")
ax1.set_ylabel("Population")

ax3.plot(t,d_pop1)
ax3.set_title("Derivative (r1)")
ax3.set_xlabel("Millions of Years")
ax3.set_ylabel("Population / Ma")

ax2.plot(t,pop2)
ax2.set_title("Civ vs T (r2)")
ax2.set_xlabel("Millions of Years")
ax2.set_ylabel("Civilizations")

ax4.plot(t,d_pop2)
ax4.set_title("Derivative (r2)")
ax4.set_xlabel("Millions of Years")
ax4.set_ylabel("Civilizations / Ma")

plt.tight_layout()
fig1.savefig('pickerism.model.pop-no-war.png')
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
