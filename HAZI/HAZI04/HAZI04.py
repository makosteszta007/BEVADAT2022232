import pandas as pn
import matplotlib.pyplot as plt
import numpy as np
##first task
def csv_to_df(df='HAZI\HAZI04\StudentsPerformance.csv'):
    df_data= pn.read_csv(df, sep=',')
    return df_data
print(csv_to_df())
##second task
def capitalize_columns(df):
    df = pn.DataFrame(df)
    df_data_capitalized = df.copy()
    df_data_capitalized.columns = [col.capitalize() if 'e' in col else col for col in df.columns]
    return df_data_capitalized
print(capitalize_columns(csv_to_df()))
##third task
def math_passed_count(df) -> int:
    df = pn.DataFrame(df)
    new_df = df.copy()
    passed = (new_df['math score']>=50).sum()
    return passed
print(math_passed_count(csv_to_df()))