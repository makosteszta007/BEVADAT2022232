import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##first task
stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
def dict_to_dataframe(test_dict):
    test_df = pd.DataFrame(test_dict)
    return test_df
##second task
def get_column(test_df,area):
    new_df = test_df.copy()
    return new_df[area]
##third task
def get_top_two(test_df):
    new_df=test_df.copy()
    return new_df.sort_values('area',ascending=False)[:2]
##fourth task
def population_density(test_df):
     new_df = test_df.copy()
     new_df['density'] = new_df['population'] / new_df['area']
     return new_df
 ##fifth task
def plot_population(test_df: pd.DataFrame) -> plt.figure:
    new_df = test_df.copy()    
    fig, ax = plt.subplots()
    ax.bar(new_df['country'], new_df['population'])
    ax.set_title('Population of Countries')
    ax.set_xlabel('Country')
    ax.set_ylabel('Population (millions)')    
    return fig
##sixth task
def plot_area(test_df: pd.DataFrame) -> plt.figure:
    new_df = test_df.copy()
    fig,ax = plt.subplots()
    ax.pie(new_df['area'], labels = new_df['country'])
    ax.set_title('Area of Countries')
    return fig