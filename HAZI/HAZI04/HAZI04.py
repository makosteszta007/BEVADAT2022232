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
##fourth task
def did_pre_course(df):
    df = pn.DataFrame(df)
    new_df = df.copy()
    df_did_precourse=new_df[new_df['test preparation course'].values == "completed"]
    return df_did_precourse
print(did_pre_course(csv_to_df()))
##fifth task
def avarage_scores(df):
    df = pn.DataFrame(df)
    new_df = df.copy()
    groupby = df.groupby('parental level of education')
    avarage_scores = groupby['math score', 'reading score', 'writing score'].mean()
    return avarage_scores
print(avarage_scores(csv_to_df()))
##sixth task
def add_age(df):
    df = pn.DataFrame(df)
    new_df = df.copy()
    np.random.seed(42)
    ages = np.random.randint(18, 67, size=len(new_df))
    new_df['age'] = ages
    return new_df
print(add_age(csv_to_df()))

