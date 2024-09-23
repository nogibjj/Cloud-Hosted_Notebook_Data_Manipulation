"""
library
"""

import pandas as pd
import matplotlib.pyplot as plt


# loading dataset
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


# Defining functions for summary statistics
def calculate_mean(df, col):
    if df[col].empty:
        return None
    return df[col].mean()


def calculate_median(df, col):
    if df[col].empty:
        return None
    return df[col].median()


def calculate_std_dev(df, col):
    if df[col].empty:
        return None
    if len(df[col]) == 1:
        return 0
    return df[col].std()


# Plotting functions
# creating a bar chart


def build_graph(
    dataframe,
    x_column,
    y_column,
    title,
    xlabel,
    ylabel,
    color="lightgray",
    jupyter_render=False,
):
    plt.figure(figsize=(12, 8))
    dataframe.plot(kind="bar", x=x_column, y=y_column, color=color, legend=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis="y")
    if not jupyter_render:
        plt.savefig("bar.png")
    else:
        plt.show()


# Build a plot on social media customer satisfaction by year
def build_graph2(
    dataframe,
    x2_col,
    y2_col,
    graph2_title,
    color="navy",
    jupyter_render=False,
):
    plt.figure(figsize=(12, 8))
    dataframe.plot(kind="bar", x=x2_col, y=y2_col, color=color, legend=False)
    plt.title(graph2_title)
    plt.grid(axis="y")
    if not jupyter_render:
        plt.savefig("bar2.png")
    else:
        plt.show()
