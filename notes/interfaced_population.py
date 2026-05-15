from pandas.io import pickle
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

PATH_STR = "./data/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx"
CACHE_STR = "./data/cache.pkl"

COLUMNS = [
    "Year",
    "Region, subregion, country or area *",
    "Total Population, as of 1 January (thousands)",
    "Births (thousands)",
]

FUNCS = {
    "Linear": lambda x: x / 50,
    "Power (a=0.3)": lambda x: (x / 50) ** 0.3,
    "Power (a=2)": lambda x: (x / 50) ** 2,
    "Exponential (k=0.1)": lambda x: (np.exp(0.1 * x) - 1) / (np.exp(5) - 1),
    "Logarithmic": lambda x: np.log(x + 1) / np.log(51),
    "Rational (a=10)": lambda x: (60 * x) / (50 * (10 + x)),
    "Smoothstep": lambda x: 3 * (x / 50) ** 2 - 2 * (x / 50) ** 3,
    "Sin S-curve": lambda x: x / 50 + (1 / np.pi) * np.sin(np.pi * x / 50),
    "Arctan (k=0.2)": lambda x: np.arctan(0.2 * x) / np.arctan(10),
}


def get_data(path):
    if Path(CACHE_STR).exists():
        # Saves a TON of time, not safe
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


def plot_func_comparison(ax, x, funcs, title="Interfacing Rate"):
    cmap = plt.get_cmap("tab20")
    colors = cmap.colors

    for i, (name, func) in enumerate(funcs.items()):
        y = func(x)
        color = colors[i % len(colors)]
        ax.plot(x, y, color=color, label=name)

    # Axis formatting
    ax.set_xlabel("Year")
    ax.set_ylabel("Normalized Rate",)
    ax.set_title(title)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.tick_params(axis="both", which="major")

    return ax.figure, ax


def create_plot(population_table):
    fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(16, 8))

    x = population_table[COLUMNS[0]][2050 - 1950 :]

    _, ax3 = plot_func_comparison(ax3, x - 2050, FUNCS)

    color = "tab:red"
    ax1.set_xlabel("Year")
    ax1.set_title("Interfaced and General Population vs Time")
    ax1.set_ylabel("Population (millions)", color=color)
    ax1.plot(x, population_table[COLUMNS[2]][2050 - 1950 :] / 1000, color=color)
    ax1.tick_params(axis="y", labelcolor=color)
    ax1.grid(True, linestyle="--", alpha=0.5)

    ax2 = ax1.twinx()

    color = "tab:blue"
    ax2.set_ylabel("Births (thousands)", color=color)
    ax2.plot(x, population_table[COLUMNS[3]][2050 - 1950 :], color=color)
    ax2.tick_params(axis="y", labelcolor=color)

    fig.tight_layout()

    return fig, (ax1, ax2)


def main(path):
    population_table = get_data(path)
    fig, axes = create_plot(population_table)
    plt.show()


if __name__ == "__main__":
    main(Path(PATH_STR))
