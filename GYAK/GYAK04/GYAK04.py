import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
##first task
stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
def dict_to_dataframe(test_dict):
    test_df = pn.DataFrame(test_dict)
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
def plot_population(test_df):
    new_df = test_df.copy()
    new_df['population'] = new_df['population'] / 1000000
    fig, ax = plt.subplots()
    ax.set_title('Population of Countries')
    ax.set_xlabel('Country')
    ax.set_ylabel('Population (millions)')
    ax.bar(new_df['Country'], new_df['population'])
    return fig