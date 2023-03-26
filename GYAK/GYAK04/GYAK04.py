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
    new_df = dict_to_dataframe(test_df)
    return new_df[area]
##third task
def get_top_two(test_df):
    test_df=dict_to_dataframe(test_df)
    return test_df.sort_values('area',ascending=False)[:2]

