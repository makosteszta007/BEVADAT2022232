import pandas as pn
import matplotlib.pyplot as plt
import numpy as np
##first task
def dict_to_dataframe(test_dict='HAZI\HAZI04\StudentsPerformance.csv'):
    test_df = pn.read_csv(test_dict, sep=",")
    return test_df
