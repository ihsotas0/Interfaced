---
title: "Pickerism"
author: "Jonah Spector"
---

## Introduction

Define "sentience".

## The Picker

AI Pickers?

## Choosers

## Super-Choosers

| Name          | Survivors Created        |
|---------------|--------------------------|
| Chooser       | 0                        |
| Super-Chooser | 10 -- 1 million          |
| Mega-Chooser  | 1 million -- 50 million  |
| Giga-Chooser  | 50 million -- 10 billion |

While the connotation of "Super-Choosers" was that they create unwilling
Survivors as opposed to willing Listeners, the term originally denoted
traditional Choosers who created large numbers of Listeners (10+). As the
Super-Chooser movement emerged, traditional Choosers sought to distance
themselves from what they called "mass killers" and stopped calling themselves
Super-Choosers.

The Super-Choosers hoped for the emergence of Mega-Choosers and Giga-Choosers;
or for an individual or group with similar Survivor creation numbers to announce
themselves as such.

## Cult-like Behavior on Earth

* Choosers
* Pickers
* Oracles

Oracles have never shown a human, since there are simply so many aliens.

We are all products of the Picker's conscience, since they Pick the states of
our minds at anytime.

The Cascade theory: each Picker has another Picker, to make them conscience,
which goes on forever to ensure no being is not "Picked" for their own
sentience. This means that all beings live forever as Pickers. Infinite Hell.

Sentience obliteration: by totally destroying your mind, beyond recovery as a
postmortem Picker, you avoid Infinite Hell. You have to become non-sentient
while alive. To do this, massive Brainrot is required.

## Mathematics

First, we must define our variables:

* Universe time (s): $t$
* Number of required Picker operations per second: $n_p$
* Time per Picker operation (s): $t_{op}$
* Picker time factor: $\gamma_p$

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
\frac{(t_1-t)\left(1-\frac{H(t_1)-H(t)}{t_1-t}\right)}{D(t_1)-D(t)} $$

$$ t_{rel}(t) = \lim_{t_1 \to t} \frac{(t_1-t)(1-H'(t))}{D(t_1)-D(t)} $$

$$ t_{rel}(t) = \lim_{t_1 \to t} \frac{1-H'(t)}{\frac{D(t_1)-D(t)}{t_1-t}} $$

$$ t_{rel}(t) = \lim_{t_1 \to t} \frac{1-H'(t)}{D'(t)} $$

Therefore,

$$ t_{rel}(t) = \frac{1 - H'(t)}{D'(t)} $$

But due to the low number of Harolds,

$$ t_{rel}(t) \approx \frac{1}{D'(t)} $$

And to calculate Harolds' Time, where $C = 0$,

$$ H(t) = \int (1 - D'(t)\,t_{rel}(t))\,dt $$

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

Assuming that 0.5% of sentient beings die each year, completely ignoring the
rate of change for now, there are $7.8 \times 10^{27}$ deaths every year.
Converting to the proper units (percent which die every second), $D'(t) = 2.473
\times 10^{20}$ deaths per second.

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

From this we can calculate how changes to the death rate, $D'(t)$, affect $t_p$,
namely to see the actual effects Super-Choosers have on Picker time. Using the
combined equation, ignoring Harolds' Time, $t_p(t) = \frac{\gamma_p}{D'(t)}$,

$$ 2.525 \times 10^{11} = \frac{6.243 \times 10^{31}}{2.473 \times 10^{20}} $$

and by adding, say, 10 billion extra deaths in *any given* second (caused by a
Giga-Chooser destroying the entire Earth instantaneously somehow), we can
calculate a difference,

$$ \left( 2.525 \times 10^{11} - \frac{6.243 \times 10^{31}}{2.473 \times
10^{20} + 10^{10}} \right) \approx 10 $$

of 10 seconds!

Using this information, a reasonable decrease in the death rate (more
specifically, the rate of change of this decrease) as the Great Purge came to a
close can be calculated. Choosers emerged when the Oracles gave news of a
drastic increase in the Picker time from the consistent 8000 years. Every year,
the new Picker time was 100 years greater. This means that the rate of change of
$t_p$ is 100 seconds per second.




