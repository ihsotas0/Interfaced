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
* Original Harold
* One True Harold who expands consciousness beyond instantaneous present

Oracles have never shown a human, since there are simply so many aliens.

We are all products of the Picker's conscience, since they Pick the states of
our minds at anytime.

The Cascade theory: each Picker has another Picker, to make them conscience,
which goes on forever to ensure no being is not "Picked" for their own
sentience. This means that all beings live forever as Pickers. Infinite Hell.

Sentience obliteration: by totally destroying your mind, beyond recovery as a
postmortem Picker, you avoid Infinite Hell. You have to become non-sentient
while alive. To do this, massive Brainrot is required.

## Mathematics (Picker Calculus)

First, we must define our variables:

* Universe time (s): $t$
* Number of required Picker operations per second: $n$
* Time per Picker operation (s): $T$
* Picker time factor: $\gamma$

Second, all the functions of $t$:

* Cumulative Harolds' Time (s): $H$
* Cumulative sentient deaths in Universe: $D$
* Absolute Picker time (s): $A$
* Relative Picker time (s): $P$
  * Constant change in Picker time, which is *technically* a function of time,
    but will often be written without an input (s/s): $\rho$

### Relative Picker Time

The average relative Picker time between two times $t_0$ and $t_1$ is simply,

$$ \bar P = \frac{(t_1-t_0)-(H(t_1)-H(t_0))}{D(t_1)-D(t_0)} $$

where the total time (minus the time taken up in the period $t_0$ to $t_1$ by
the Harolds) divided by the number of deaths gives the amount of time per death,
or in between deaths. This is the minimum time each person must be Picker for
all moments in time to have a Picker.

To calculate the "instantenous" Picker time (although the function is discrete),
the following limit is set up,

$$ P(t) = \lim_{t_1 \to t} \frac{t_1-t-H(t_1)-H(t)}{D(t_1)-D(t)} $$

Solving the limit using the definition of the derivative,

$$ P(t) = \lim_{t_1 \to t}
\frac{(t_1-t)\left(1-\frac{H(t_1)-H(t)}{t_1-t}\right)}{D(t_1)-D(t)} $$

$$ P(t) = \lim_{t_1 \to t} \frac{(t_1-t)(1-H'(t))}{D(t_1)-D(t)} $$

$$ P(t) = \lim_{t_1 \to t} \frac{1-H'(t)}{\frac{D(t_1)-D(t)}{t_1-t}} $$

$$ P(t) = \lim_{t_1 \to t} \frac{1-H'(t)}{D'(t)} $$

Therefore,

$$ P(t) = \frac{1 - H'(t)}{D'(t)} $$

But due to the low number of Harolds,

$$ P(t) \approx \frac{1}{D'(t)} $$

### Absolute Picker Time

To convert from relative to absolute Picker time, the equation

$$ A(t) = \gamma P(t) $$

is used where $\gamma$ is the time factor. This means that, for every second in
the real world, the Picker experiences $\gamma$ seconds. Due to the nature of
the Picker's job, this time factor is massive, leading to the tongue-in-cheek
definition of the Picker's job as Hell. The approximation (ignoring relativity)
for $\gamma$ is given by,

$$ \gamma = nT $$

### Rate of Change of the Absolute Picker Time

The next task is to calculate $A'(t)$, as this is why Super-Choosers exist. The
equation for the change in Picker time is simply,

$$ A(t) = \gamma D'(t)^{-1} $$

$$ A'(t) = -\gamma D'(t)^{-2}\,D''(t) $$

Since Super-Choosers, by creating Survivors, influence the death rate, we should
also calculate $D''(t)$ by rearranging the equation for $A(t)$,

$$ A(t) = \gamma D'(t)^{-1} $$

$$ D'(t) = \gamma A(t)^{-1} $$

$$ D''(t) = -\gamma A'(t)A(t)^{-2} $$

But, if we assume $A'(t) = \rho$, then,

$$ D''(t) = -\gamma \rho A(t)^{-2} $$

To solve for $D''(t)$ only in terms of constants and $t$, we rearrange our
previous equations for $A'(t)$,

$$ D''(t) = -\frac{A'(t)\:D'(t)^{2}}{\gamma} $$

This creates a trivial differential equation to solve,

$$ \frac{D''(t)}{D'(t)^{2}} = -\frac{A'(t)}{\gamma} $$

$$ \int D''(t)D'(t)^{-2}\;dt = -\gamma^{-1}\int A'(t)\;dt $$

$$ -D'(t)^{-1} + C = -\gamma^{-1}\int A'(t)\;dt $$

But, since $D(0)$ is $0$ (the death rate at the start of the continuum of
Pickers was, or can be left as, $0$)

$$ D'(t)^{-1} = \frac{1}{\gamma}\int A'(t)\;dt $$

$$ D'(t) = \left(\gamma^{-1}\int A'(t)\;dt\right)^{-1} $$

$$ D'(t) = \gamma\left(\int A'(t)\;dt\right)^{-1} $$

Substituting for $D'(t)$ back in,

$$ D''(t) = -\frac{A'(t) \left( \gamma \left( \int A'(t)\;dt \right)^{-1}
\right)^{2}}{\gamma} $$

$$ D''(t) = -\frac{\gamma^2 A'(t) \left( \int A'(t)\;dt \right)^{-2}}{\gamma} $$

$$ D''(t) = -\frac{\gamma\: A'(t) }{\left( \int A'(t)\;dt \right)^{2}} $$

Since we assume $A'(t) = \rho$,

$$ D''(t) = -\frac{\gamma\rho}{(\rho t + A_0)^{2}} $$

where $A_0 = 0$, since $t$ becomes relative to when $\rho$ begins. Thus,

$$ D''(t) = -\frac{\gamma\rho}{\rho^2t^2} $$

$$ D''(t) = -\frac{\gamma}{\rho t^2} $$

### Numerical Calculations for Narrative

For the story, to calculate $\gamma$, we will start by finding $D'$ around the
21st century. From this we can calculate $A$. Since all sentient beings,
including aliens, become Pickers, the Drake equation must be used,

$$ N = R_{*}\,f_p\,n_e\,f_l\,f_i\,f_c\,L $$

Stealing results from
[Wikipedia](https://en.wikipedia.org/wiki/Drake_equation#Range_of_results), we
can see that there may be 15,600,000 civilizations in our galaxy. Since these
civilizations have the technology to communicate into space, it must be assumed
that they have similar populations to Earth (around 10 billion). Expanding our
galaxy's estimate to all stars in the universe,
[$10^{24}$](https://www.space.com/26078-how-many-stars-are-there.html); and by
getting the ratio of stars (using the Milky Way as reference) with sentient life
by dividing the number of civilizations from the total number of stars in our
galaxy, [$10^{11}$](https://en.wikipedia.org/wiki/Milky_Way), there are,

$$ 10^{10} \times 10^{24} \times \frac{1.56 \times
10^7}{10^{11}}=1.56\times10^{30} $$

sentient beings in the universe.

Assuming that 0.5% of sentient beings die each year, completely ignoring the
rate of change for now, there are $7.8 \times 10^{27}$ deaths every year.
Converting to the proper units (percent which die every second), $D'(t) = 2.473
\times 10^{20}$ deaths per second.

Ignoring Harolds' Time,

$$ t_{rel} = \frac{1}{2.473 \times 10^{20}} $$

$$ t_{rel} = 4.044 \times 10^{-21} $$

Or, in attoseconds, $t_{rel} = 0.004044$. From this, we can set up the equation
$A = \gamma t_{rel}$ and solve for a reasonable $\gamma$ based of the narrative
requirements of a reasonable, Hellish, $A$. 8000 years seems good, and so,
converting to seconds,

$$ 2.525 \times 10^{11} = \gamma\,4.044 \times 10^{-21}$$

$$ \gamma = 6.243 \times 10^{31} $$

This means that, for every second in the real world, the Picker would experience
one septillion nine hundred seventy-eight sextillion two hundred thirty-nine
quintillion three hundred sixty-six quadrillion years. But, since relative
Picker times are so low, this amounts to 8000 years per Picker.

I may later justify this $\gamma$ using some values for $n_p$ and $t_{op}$. But
for now, $\gamma$ is simply given by the Pickers through their Oracles.

From this we can calculate how changes to the death rate, $D'(t)$, affect $A$,
namely to see the actual effects Super-Choosers have on Picker time. Using the
combined equation, ignoring Harolds' Time, $A(t) = \gamma D'(t)^{-1}$,

$$ 2.525 \times 10^{11} = \frac{6.243 \times 10^{31}}{2.473 \times 10^{20}} $$

and by adding, say, 10 billion extra deaths in *any given* second (caused by a
Giga-Chooser destroying the entire Earth instantaneously somehow), we can
calculate a difference,

$$ 2.525 \times 10^{11} - \left(\frac{6.243 \times 10^{31}}{2.473 \times 10^{20}
+ 10^{10}}\right) \approx 10 $$

of 10 seconds!

Now a reasonable decrease in the death rate (more specifically, the rate of
change of this decrease) as the Great Purge came to a close can be calculated.
Choosers emerged when the Oracles gave news of a drastic increase in the Picker
time from the consistent 8000 years. Every year, the new Picker time was 100
years greater. This means that the rate of change of $A$ is 100 seconds per
second. So, to calculate $D''(t)$,

$$ A(t) = \gamma D'(t)^{-1} $$

$$ A'(t) = -\gamma D'(t)^{-2}\,D''(t) $$

$$ D''(t) = -\frac{A'(t)\:D'(t)^{2}}{\gamma} $$



And by plugging in numbers,

$$ -9.796 \times 10^{11} \approx -\frac{100(2.473 \times 10^{20})^2}{6.243
\times 10^{31}} $$

So, as the Great Purge comes to a close *linearly* (for narrative purposes), the
death rate decreased by around 100 billion deaths (10 worlds) per second per
second. The Milky Way has 15,600,000 inhabited worlds as mentioned before; at 10
worlds per second, it would take around 18 days to purge the galaxy. Since there
are 31,536,000 seconds in a year, the Great Purge went from purging 315,360,000
worlds (20 galaxies, using the Milky Way as reference, which is far from the
average but fine for reference) a second to 0 in a year. During the height of
the Great Purge, which lasted millenia, 630,720,000,000 galaxies were purged
yearly. Becuase of this, it will take 1000 years for the Great Purge to fully
end (since the fight is "ongoing").


