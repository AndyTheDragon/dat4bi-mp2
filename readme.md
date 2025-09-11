# Datamatiker Business Intelligence Mini Project 2
This project consists of two parts; the MP2_report where we explore the datasets and comment on the results, and the WineDataExplorerPackage with a collection of functions used in the report.
## The report

## The WineDataExplorerPackage
Contains functions to read the data from the Excel (xlsx) files into a Pandas Dataframe, doing some basic cleaning, like checking for missing or NaN values. And then a lot of functions to create different representations of the descriptive statistics and other analysis of the data.

### Reading (and cleaning) the data
`read_data_to_dataframe(file_path, winetype) -> pd.DataFrame`
Reads the Excel file, checks for missing values and returns a Datafram
`combine_dataframes(dfs) -> pd.DataFrame`
Combines a list of Dataframes into a single Datafram
`remove_duplicates(df: pd.DataFrame) -> pd.DataFrame`
Removes duplicate entries from the dataframe

### Descriptive statistics
`describe_wine_data(df: pd.DataFrame, verbose: bool = True, round_digits: int = 0) -> pd.DataFrame`
Prints a table of the most commonly descriptive statistical markers for each column in the Dataframe, also returns the statics as a Dataframe, in case further computation is necessary.

### Plots
`show_boxplots(df: pd.DataFrame, layout: str = "separate")`
Forklaring
`show_histograms(df: pd.DataFrame, bins: int = 10, layout: str = "separate", bell_curve: bool = False)`
FOrklaring
`show_scatter_matrix(df: pd.DataFrame, figsize: tuple = (12, 12), diagonal: str = "hist")`
FOrklaring
`show_correlation_heatmap(df: pd.DataFrame)`
Teskt
```python
show_grouped_histograms(
    df: pd.DataFrame,
    bins: int = 10,
    layout: str = "separate",
    category_col: str = "type",
    bell_curve: bool = True,
    max_cols: int = 3,
    alpha: float = 0.7,
)
```
Forklaring
