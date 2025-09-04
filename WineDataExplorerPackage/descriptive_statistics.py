import pandas as pd

def describe_wine_data(df: pd.DataFrame, verbose: bool = True, round_digits: int = 0) -> pd.DataFrame:
    """
    Generates descriptive statistics for the wine DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame containing wine data.
        verbose (bool): If True, prints the summary to the console.
        round_digits (int): If >0, round numeric values to this many decimals.
                            If 0, leave values as-is. Defaults to 0.

    Returns:
        pd.DataFrame: DataFrame with descriptive statistics.
    """
    wine_summary = df.describe(include='all').transpose()
    wine_summary = wine_summary.drop(
        columns=[c for c in ['unique', 'top', 'freq'] if c in wine_summary.columns],
        errors="ignore"
    )

    if round_digits > 0:
        wine_summary = wine_summary.round(round_digits)

    if 'count' in wine_summary.columns:
        wine_summary['count'] = wine_summary['count'].astype('Int64')

    wine_summary.index.name = "feature"

    if verbose:
        print(f"Summary: {df.shape[0]} rows × {df.shape[1]} columns")
        print(wine_summary.to_string())

    return wine_summary


