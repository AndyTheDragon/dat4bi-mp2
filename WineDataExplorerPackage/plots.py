import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def show_boxplots(df: pd.DataFrame, layout: str = "separate"):
    """
    Displays boxplots for all numeric columns in the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        layout (str): 'separate' = one plot per column,
                      'grid' = all plots in a grid.
    """
    numeric_cols = df.select_dtypes(include="number").columns

    if layout == "grid":
        n = len(numeric_cols)
        rows = (n + 2) // 3
        fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
        axes = axes.flatten()

        for i, col in enumerate(numeric_cols):
            df.boxplot(column=col, ax=axes[i])
            axes[i].set_title(f'Boxplot for {col}')
            axes[i].set_ylabel(col)

        for j in range(i + 1, len(axes)):
            axes[j].axis("off")

        plt.tight_layout()
        plt.show()
    else:
        for column in numeric_cols:
            plt.figure(figsize=(6, 4))
            df.boxplot(column=column)
            plt.title(f'Boxplot for {column}')
            plt.ylabel(column)
            plt.tight_layout()
            plt.show()


def show_histograms(df: pd.DataFrame, bins: int = 10):
    """
    Displays histograms for all numeric columns in the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        bins (int): Number of bins for histograms. Defaults to 10.
    """
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        df[col].hist(bins=bins)
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()


def show_scatter_matrix(df: pd.DataFrame, figsize: tuple = (12, 12), diagonal: str = "hist"):
    """
    Displays a scatter matrix (pairplot) for numeric columns.

    Args:
        df (pd.DataFrame): Input DataFrame.
        figsize (tuple): Size of the figure. Defaults to (12, 12).
        diagonal (str): Plot type on the diagonal ('hist' or 'kde'). Defaults to 'hist'.
    """
    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) < 2:
        print("Scatter matrix requires at least two numeric columns.")
        return
    scatter_matrix(df[numeric_cols], figsize=figsize, diagonal=diagonal)
    plt.suptitle("Scatter Matrix of Numeric Features")
    plt.show()
