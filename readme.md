# Datamatiker Business Intelligence Mini Project 2
This project consists of two parts; the MP2_report where we explore the datasets and comment on the results, and the WineDataExplorerPackage with a collection of functions used in the report.
## The report
This report explores and visualizes two datasets of Portuguese red and white "Vinho Verde" wines. The analysis begins by cleaning and merging the data, ensuring all values are numeric and free of errors. Descriptive statistics and visualizations, such as histograms, boxplots and barplots are used to compare chemical properties and quality scores between red and white wines

Key findings include:

- White wines generally have higher residual sugar, alcohol and density score.
- Reds tend to me more acidic and have higher volatile acidity and sulphates
- Both wines peak around quality levels 5-6, but whites have a slight edge in average quality
- Alcohol content is stronger correlated to quality than sugar

The report uses custom plotting functions to efficiently display results, making it easy to spot trends and differences.
Overall, the analysis provides a clear comparison between red and white wines, highligting the chemical factors most associated with wine quality.


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
#### show_boxplots
```python
show_boxplots(df: pd.DataFrame, layout: str = "separate")
```
A custom method that displays boxplots for all numeric columns in the dataframe given as parameter.
A parameter `layout: str = ""` has been added in order to be able to display all the boxplots in one big frame, instead of having them drawn one by one, and thus taking up a lot of space in the report.
#### show_histograms
```python
show_histograms(df: pd.DataFrame, bins: int = 10, layout: str = "separate", bell_curve: bool = False)
```
Displays histograms for all numeric columns in the dataframe. The layout parameter allows you to show all histograms together or separately. Optionally, a bell curve can be overlaid, if `bell_curve: bool = True` to visualize the normal distribution for each column.
#### show_scatter_matrix
```python
show_scatter_matrix(df: pd.DataFrame, figsize: tuple = (12, 12), diagonal: str = "hist")
```
Draws a scatter matrix (pairplot) for all numeric columns in the dataframe. Useful for visualizing relationships and correlations between multiple variables at once.
#### show_correlation_heatmap
```Python
show_correlation_heatmap(df: pd.DataFrame)
```
Displays a heatmap of the correlation matrix for all numeric columns in the dataframe. The map is colored from red (+1) to blue (-1) in order to make it easy and accesible for the human eye to spot correlations between two values.
#### show_grouped_histograms
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
Draws side-by-side histograms for all numeric columns, grouped by a categorical column (e.g., wine type). Each group can have its own bell curve overlay by setting `bell_curve: bool = True`. The layout and number of columns per row can be customized for compact visualization.
#### show_binned_data
```python
show_binned_data(
    df: pd.DataFrame,
    bins: int = 5,
    column_to_bin: str = 'pH',
    column_to_plot: str = 'density',
    aggregation_method: str = 'mean'
)
```
Bins a specified column (e.g., pH) into a chosen number of intervals and plots the aggregated values (mean or max) of another column (e.g., density) for each bin. Useful for comparing how an attribute varies across different ranges.