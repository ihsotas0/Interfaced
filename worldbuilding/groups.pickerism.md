---
title: "Pickerism"
author: "Jonah Spector"
---

* Choosers
* Pickers
* Oracles

Oracles have never shown a human, since there are simply so many aliens.

## Mathematics

First, we must define our variables:

* Universe time (s): $t$
* Number of required Picker operations per second: $n_p$
* Time per Picker operation (s): $t_{op}$
* Picker time factor: $\gamma_p$
* Ratio of population which dies every second (assumed constant for
  calculations): $r_D$

Second, all the functions of $t$:

* Cumulative Harolds' Time (s): $H$
* Cumulative sentient deaths in Universe: $D$
* Absolute Picker time (s): $t_p$
* Relative Picker time (s): $t_{rel}$

The average relative Picker time between two times $t_0$ and $t_1$ is simply,

$$ \bar t_{rel} = \frac{(t_1-t_0)-(H(t_1)-H(t_0))}{D(t_1)-D(t_0)} $$

where the total time (minus the time taken up in the period $t_0$ to $t_1$ by
the Harolds) divided by the number of deaths gives the amount of time per death,
or in between deaths. This is the minimum time each person must be Picker for
all moments in time to have a Picker. The Harolds, of course, go beyond this
minimum for the sake of others, and so their time is accounted for by reducing
the amount of time which must be allotted to all those who died in the period.

To calculate the "instantenous" Picker time (although the function is discrete),
the following limit is set up,

$$ t_{rel}(t) = \lim_{t_1 \to t} \frac{t_1-t-H(t_1)-H(t)}{D(t_1)-D(t)} $$

Solving the limit using the definition of the derivative,

$$ t_{rel}(t) = \lim_{t_1 \to t}
\frac{(t_1-t)(1-\frac{H(t_1)-H(t)}{t_1-t})}{D(t_1)-D(t)} $$

$$ t_{rel}(t) = \lim_{t_1 \to t} \frac{(t_1-t)(1-H'(t))}{D(t_1)-D(t)} $$

$$ t_{rel}(t) = \lim_{t_1 \to t} \frac{1-H'(t)}{\frac{D(t_1)-D(t)}{t_1-t}} $$

$$ t_{rel}(t) = \lim_{t_1 \to t} \frac{1-H'(t)}{D'(t)} $$

Therefore,

$$ t_{rel}(t) = \frac{1 - H'(t)}{D'(t)} $$

But due to the low number of Harolds,

$$ t_{rel}(t) \approx \frac{1}{D'(t)} $$

And to calculate Harolds' Time, where $C = 0$,

$$ H(t) = \int 1 - D'(t)\,t_{rel}(t)\,dt $$

I don't know if it is possible to solve this integral, but numerical solutions
work since the function is *technically* discrete (although with the number of
deaths per second being so high, it is basically continous).

To convert from relative to absolute Picker time, the equation $t_p = \gamma_p
t_{rel}$ is used where $\gamma_p$ is the time factor. This means that, for every
second in the real world, the Picker experiences $\gamma_p$ seconds. Due to the
nature of the Picker's job, this time factor is massive, leading to the
tongue-in-cheek definition of the Picker's job as Hell. The approximation
(ignoring relativity) for $\gamma_p$ is given by $\gamma_p = n_p t_{op}$. This
approximation is unused as $\gamma_p$ arises from the narrative.

For the story, to calculate $\gamma_p$, we will start by finding $D'(t)$ and
$D''(t)$ around the 21st century. From this we can calculate $t_{rel}(t)$. Since
all sentient beings, including aliens, become Pickers, the Drake equation must
be used,

$$ N = R_{*}\,f_p\,n_e\,f_l\,f_i\,f_c\,L $$

Stealing results from
[Wikipedia](https://en.wikipedia.org/wiki/Drake_equation#Range_of_results), we
can see that there may be 15,600,000 civilizations in our galaxy. Since these
civilizations have the technology to communicate into space, it must be assumed
that they have similar populations to Earth (around 10 billion). Expanding our
galaxy's estimate to all stars in the universe,
[$10^{24}$](https://www.space.com/26078-how-many-stars-are-there.html), and by
getting the ratio of stars in our galaxy with sentient life from the total,
[$10^{11}$](https://en.wikipedia.org/wiki/Milky_Way), there are,

$$P=10^{10}\times10^{24}\times\frac{1.56\times10^7}{10^{11}}=1.56\times10^{30}$$

sentient beings in the universe. Exactly one nonillion five hundred sixty
octillion.

Assuming that 0.5% of sentient beings die each year (related to $r_D$ which is
the death ratio every second), completely ignoring the rate of change for now,
there are $7.8 \times 10^{27}$ deaths every year. Converting to the proper
units, $D'(t) = r_D\,D(t) = 2.473 \times 10^{20}$ deaths per second.

Ignoring Harolds' Time,

$$ t_{rel} = \frac{1}{2.473 \times 10^{20}} $$

$$ t_{rel} = 4.044 \times 10^{-21} $$

Or, in attoseconds, $t_{rel} = 0.004044$. From this, we can set up the equation
$t_p = \gamma_p t_{rel}$ and solve for a reasonable $\gamma_p$ based of the
narrative requirements of a reasonable, Hellish, $t_p$. 8000 years seems good,
and so, converting to seconds,

$$ 2.525 \times 10^{11} = \gamma_p\,4.044 \times 10^{-21}$$

$$ \gamma_p = 6.243 \times 10^{31} $$

This means that, for every second in the real world, the Picker would experience
one septillion nine hundred seventy-eight sextillion two hundred thirty-nine
quintillion three hundred sixty-six quadrillion years. But, since relative
Picker times are so low, this amounts to 8000 years per Picker.

I may later justify this $\gamma_p$ using some values for $n_p$ and $t_{op}$.
But for now, $\gamma_p$ is simply given by the Pickers through their Oracles.
