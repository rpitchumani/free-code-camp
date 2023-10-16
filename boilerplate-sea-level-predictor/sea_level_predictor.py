import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.scatter(
        x=df["Year"],
        y=df["CSIRO Adjusted Sea Level"]
    )

    # Create first line of best fit
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    res_1 = linregress(x, y)
    slope_1 = res_1.slope
    intercept_1 = res_1.intercept

    years = np.arange(1880, 2051, 1)
    sea_level = slope_1 * years + intercept_1

    ax.plot(
        years,
        sea_level,
        "-",
        c="red"
    )

    # Create second line of best fit

    df_2000 = df[df["Year"] >= 2000]
    x = df_2000["Year"]
    y = df_2000["CSIRO Adjusted Sea Level"]

    res_2 = linregress(x, y)
    slope_2 = res_2.slope
    intercept_2 = res_2.intercept

    years = np.arange(2000, 2051, 1)
    sea_level = slope_2 * years + intercept_2

    ax.plot(
        years,
        sea_level,
        "-",
        c="green"
    )

    # Add labels and title

    ax.set(
        title = "Rise in Sea Level",
        xlabel = "Year",
        ylabel = "Sea Level (inches)"
    )
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()