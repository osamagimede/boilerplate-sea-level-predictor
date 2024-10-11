import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df.head())
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # from 1880 to 2050
    sea_level_fit = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_fit, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit
    data_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
    years_extended_a = pd.Series(range(2000, 2051)) # from 1850 to 2076
    sea_level_fit_recent = slope_recent * years_extended_a + intercept_recent
    plt.plot(years_extended_a, sea_level_fit_recent, color='green', label='Best Fit Line (2000 Onwards)')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.xlim(1850, 2075)
    #plt.ylim(bottom=0)  # Start y-axis at 0 for better visualization
    plt.grid()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()