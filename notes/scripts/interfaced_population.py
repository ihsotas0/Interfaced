# Citation: United Nations, Department of Economic and Social Affairs, Population Division (2024). *World Population Prospects 2024, Online Edition.*

import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import math

PATH_STR = "../data/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx"
CACHE_STR = "../data/cache.pkl"

WAR_DEATHRATE = np.array([0.1, 0.1, 0.05])

COLUMNS = [
    "Year",
    "Region, subregion, country or area *",
    "Total Population, as of 1 January (thousands)",
    "Births (thousands)",
    "Life Expectancy at Birth, both sexes (years)",
]

# All functions satisfy:
# f(0) = 0
# f(50) = 1
# monotonically increasing on [0, 50]


def normalize01(f):
    """Normalize any f(x) so f(0)=0 and f(50)=1."""
    f0 = f(0)
    f50 = f(50)
    return lambda x: (f(x) - f0) / (f50 - f0)


FUNCS = {
    # --- Baselines ---
    "Linear": lambda x: x / 50,
    # --- Power families ---
    # "Power (0.5)": lambda x: (x / 50) ** 0.5,     # early acceleration
    # "Power (2)": lambda x: (x / 50) ** 2,         # late acceleration
    # "Power (3)": lambda x: (x / 50) ** 3,
    # "Power (5)": lambda x: (x / 50) ** 5,
    # # --- Exponential families ---
    # "Exponential Mild": normalize01(
    #     lambda x: np.exp(0.05 * x)
    # ),
    # "Exponential Strong": normalize01(
    #     lambda x: np.exp(0.12 * x)
    # ),
    # # --- Logarithmic / diminishing returns ---
    # "Logarithmic": normalize01(
    #     lambda x: np.log(x + 1)
    # ),
    # # --- Rational saturation ---
    # "Rational (a=5)": lambda x: (11 * x) / (50 * (5 + x)),
    # "Rational (a=20)": lambda x: (70 * x) / (50 * (20 + x)),
    # --- Smooth polynomial S-curves ---
    # "Smoothstep": lambda x: (
    #     3 * (x / 50) ** 2
    #     - 2 * (x / 50) ** 3
    # ),
    # "Smootherstep": lambda x: (
    #     6 * (x / 50) ** 5
    #     - 15 * (x / 50) ** 4
    #     + 10 * (x / 50) ** 3
    # ),
    # # --- Logistic / sigmoid ---
    # "Logistic Mild": normalize01(
    #     lambda x: 1 / (1 + np.exp(-0.15 * (x - 25)))
    # ),
    "Logistic Strong": normalize01(lambda x: 1 / (1 + np.exp(-0.30 * (x - 25)))),
    # --- Gompertz (technology adoption style) ---
    "Gompertz": normalize01(lambda x: np.exp(-5 * np.exp(-0.10 * x))),
    # --- Weibull CDF ---
    "Weibull": normalize01(lambda x: 1 - np.exp(-((x / 20) ** 2))),
    # # --- Arctangent ---
    # "Arctan": normalize01(
    #     lambda x: np.arctan(0.15 * x)
    # ),
    # # --- Sinusoidal easing ---
    # "Sine Ease-In": lambda x: 1 - np.cos((np.pi / 2) * (x / 50)),
    # "Sine Ease-Out": lambda x: np.sin((np.pi / 2) * (x / 50)),
    # "Sine Ease-In-Out": lambda x: (
    #     0.5 - 0.5 * np.cos(np.pi * x / 50)
    # ),
    # --- Error function (diffusion-like) ---
    "Erf": normalize01(lambda x: np.vectorize(math.erf)((x - 25) / 10)),
    # --- Hill function (network effects) ---
    "Hill (n=2)": normalize01(lambda x: (x**2) / (15**2 + x**2)),
    "Hill (n=4)": normalize01(lambda x: (x**4) / (20**4 + x**4)),
}


def get_data(path):
    if Path(CACHE_STR).exists():
        # Saves a TON of time, not safe. Delete *.pkl if cache doesn't match new df requirements
        return pd.read_pickle(Path(CACHE_STR))

    with pd.ExcelFile(path) as xls:
        sheets = ["Estimates", "Medium variant"]
        dfs = []

        for sheet in sheets:
            df = pd.read_excel(xls, sheet, skiprows=16, usecols=COLUMNS)
            df = df.loc[lambda x: x[COLUMNS[1]] == "World"]
            df = df.drop(columns=[COLUMNS[1]])
            df[COLUMNS[2:]] = df[COLUMNS[2:]].apply(pd.to_numeric, errors="coerce")
            dfs.append(df)

        cache_df = pd.concat(dfs, ignore_index=True)
        cache_df.to_pickle(Path(CACHE_STR))

        return cache_df


# To compare FUNCS for picking a nice looking one
def plot_func_comparison(ax, x, funcs, title="Interfacing Rate"):
    cmap = plt.get_cmap("tab20")
    colors = cmap.colors

    for i, (name, func) in enumerate(funcs.items()):
        y = func(x)
        color = colors[i % len(colors)]
        ax.plot(x + 2050, y, color=color, label=name)

    ax.set_ylabel(
        "Normalized Rate",
    )
    ax.set_title(title)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)

    return ax.figure, ax


def population_projection(x, e0, df, func_str, war_deathrate):
    # Interfacing rate for each year
    y = FUNCS[func_str](x - 2050)
    in_births = y * df[COLUMNS[3]]

    n_years = len(x)
    in_pop = np.zeros(n_years)
    in_adult_pop = np.zeros(n_years)
    in_deaths = np.zeros(n_years)

    # Track all cohorts as arrays
    cohort_populations = np.zeros(n_years)  # population of each cohort
    cohort_survival = np.zeros(n_years)  # survival probability of each cohort
    n_cohorts = 0  # number of active cohorts

    for year_idx in range(n_years):
        birth = in_births.iloc[year_idx]
        life_exp = e0[year_idx]

        # Approx annual survival probability
        annual_survival = 1 - 1 / life_exp

        # Add new cohort
        cohort_populations[n_cohorts] = birth
        cohort_survival[n_cohorts] = annual_survival
        n_cohorts += 1

        # Update populations of all existing cohorts
        survivors = cohort_populations[:n_cohorts] * cohort_survival[:n_cohorts]
        deaths = cohort_populations[:n_cohorts] - survivors

        # Apply war death rate for adults (age >= 18)
        ages = np.arange(n_cohorts)  # cohort age in years
        adult_mask = ages >= 18
        if year_idx < len(war_deathrate):
            war_deaths = survivors[adult_mask] * war_deathrate[year_idx]
            survivors[adult_mask] -= war_deaths
            deaths[adult_mask] += war_deaths

        # Store totals for this year
        in_pop[year_idx] = survivors.sum()
        in_adult_pop[year_idx] = survivors[adult_mask].sum()
        in_deaths[year_idx] = deaths.sum()

        # Update cohorts for next iteration
        cohort_populations[:n_cohorts] = survivors

    return in_pop, in_births, in_deaths, in_adult_pop


def create_plot(population_table, func_str="Hill (n=2)"):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

    # Trim years below 2050
    df = population_table[:][2050 - 1950 :].reset_index(drop=True)

    # Years
    x = df[COLUMNS[0]]

    e0 = df[COLUMNS[4]].to_numpy()

    # No war deathrate to start with
    war_deathrate = np.zeros(e0.shape)

    in_pop, in_births, in_deaths, in_adult_pop = population_projection(
        x, e0, df, func_str, war_deathrate
    )

    # "this ratio of people over 18 died during the war during this year"
    war_deathrate[20] = WAR_DEATHRATE[0]  # 2070
    war_deathrate[21] = WAR_DEATHRATE[1]  # 2071
    war_deathrate[22] = WAR_DEATHRATE[2]  # 2072

    war_in_pop, war_in_births, war_in_deaths, war_in_adult_pop = population_projection(
        x, e0, df, func_str, war_deathrate
    )

    # --- Plot Populations ---
    ax1.set_title("Global Interfaced Population vs Time")
    ax1.set_ylabel("Population [billions]")
    # ax1.plot(
    #     x,
    #     df[COLUMNS[2]] / (1000**2),
    #     color="green",
    #     label="Total Population",
    # )
    ax1.plot(
        x, np.cumsum(in_births) / (1000**2), label="Raw In. Population", color="black"
    )
    ax1.plot(
        x,
        in_pop / (1000**2),
        label=f"In. Population\n(with mortality approx.)",
        color="red",
    )
    ax1.plot(
        x,
        war_in_pop / (1000**2),
        label=f"In. Population\n(with war)",
        linestyle="--",
        color="red",
    )
    ax1.plot(
        x,
        in_adult_pop / (1000**2),
        label=f"In. Adult Population\n(with mortality approx.)",
        color="blue",
    )
    ax1.plot(
        x,
        war_in_adult_pop / (1000**2),
        label=f"In. Adult Population\n(with war)",
        linestyle="--",
        color="blue",
    )
    ax1.legend()
    ax1.grid(True, linestyle="--", alpha=0.5)

    # --- Plot Births ---
    ax2.set_title("Global Birthrate vs Time")
    ax2.set_ylabel("Births [millions/year]")
    ax2.plot(
        x,
        df[COLUMNS[3]] / 1000,
        label="Total Births",
        color="black",
    )
    ax2.plot(x, in_births / 1000, label="Interfaced Births", color="blue")
    ax2.legend()
    ax2.grid(True, linestyle="--", alpha=0.5)

    # --- Plot Deathrate ---
    ax3.set_title("Interfaced Deathrate vs Time")
    ax3.set_ylabel("Deaths [millions/year]")
    ax3.plot(x, in_deaths / 1000, label="Baseline mortality approx.")

    war_dead = sum(war_in_deaths[20:24] - in_deaths[20:24])

    # Thousand -> Million
    war_dead /= 1000

    ax3.plot(x, war_in_deaths / 1000, label=f"War ({int(war_dead)} million In. deaths)")
    ax3.fill_between(
        x[:24],
        in_deaths[:24] / 1000,
        war_in_deaths[:24] / 1000,
        alpha=0.1,
        color="black",
    )
    ax3.legend()
    ax3.grid(True, linestyle="--", alpha=0.5)

    # --- Plot Interfacing Rate ---
    ax4 = plot_func_comparison(
        ax4, x - 2050, FUNCS, title=f"Interfacing Rate Function Selected: {func_str}"
    )

    fig.suptitle(
        f"""Interfaced Population Projections Using 'World Population Prospects, 2024' (UN)
            War is from 2070 to 2072, with {WAR_DEATHRATE[0] * 100}%, {WAR_DEATHRATE[1] * 100}%, and {WAR_DEATHRATE[2] * 100}% of In. adults dying in each respective year.
            Only In. adults die in the war. War deaths do not include Un-Interfaced people.
        """,
    )
    fig.supxlabel(f"Time [year]")
    fig.tight_layout()
    return fig, (ax1, ax2, ax3, ax4)


def main(path):
    population_table = get_data(path)
    fig, axes = create_plot(population_table)
    plt.show()


if __name__ == "__main__":
    main(Path(PATH_STR))
