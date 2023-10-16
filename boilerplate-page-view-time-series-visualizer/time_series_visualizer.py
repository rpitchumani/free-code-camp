import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0)
df.index = pd.to_datetime(df.index, format="%Y-%m-%d")

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=[12, 4])

    ax.plot(df.index, df["value"], c="red")

    ax.set(
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
        xlabel="Date",
        ylabel="Page Views"
    )

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    dates_in_order = pd.date_range(start="2022-01-01", end="2022-12-01", freq="MS")
    months_in_order = dates_in_order.map(lambda x: x.month_name()).to_list()

    df_grp = df.copy()
    df_grp["year"] = df.index.year
    df_grp["month_name"] = df.index.strftime("%B")
    df_grp["Months"] = pd.Categorical(
        df_grp["month_name"],
        categories=months_in_order,
        ordered=True
    )

    df_bar = pd.pivot_table(
        df_grp,
        values="value",
        index="year",
        columns="Months",
        aggfunc="mean"
    )

    # Draw bar plot
    fig = df_bar.plot(
        kind="bar",
        legend=True,
    ).figure

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    dates_in_order = pd.date_range(start="2022-01-01", end="2022-12-01", freq="MS")
    months_in_order = dates_in_order.map(lambda x: x.month_name().str.slice(stop=3)).to_list()

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    sns.set(style="white")

    fig, ax = plt.subplots(1, 2, figsize=[14, 6])

    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        hue="year",
        palette="deep",
        legend=False,
        ax=ax[0]
    )

    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        hue="month",
        palette="deep",
        order=months_in_order,
        legend=False,
        ax=ax[1]
    )

    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")

    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
