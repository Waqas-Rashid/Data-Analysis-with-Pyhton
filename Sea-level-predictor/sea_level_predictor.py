import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    plt.scatter(x = x1 ,y = y1)
    # Create first line of best fit
    res = linregress(x1, y1)
    plt.plot(range(1880, 2051), res.intercept + res.slope*range(1880, 2051), 'r', label='fitted line')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    res2 = linregress(x2, y2)
    plt.plot(range(2000, 2051), res2.intercept + res2.slope*range(2000, 2051), 'r', label='2nd fitted line')

    # Add labels and title
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()