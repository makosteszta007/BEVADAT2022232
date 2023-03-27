import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
##first task
def csv_to_df(df='HAZI\HAZI04\StudentsPerformance.csv'):
    df_data= pd.read_csv(df, sep=',')
    return df_data
##second task
def capitalize_columns(df: pd.DataFrame) -> pd.DataFrame:   
    df_data_capitalized = df.copy()
    df_data_capitalized.columns = [col.capitalize() if 'e' not in col else col for col in df.columns]
    return df_data_capitalized
##third task
def math_passed_count(df: pd.DataFrame) -> int:
    new_df = df.copy()    
    passed = (new_df['math score']>=50).sum()
    return passed
##fourth task
def did_pre_course(df: pd.DataFrame):    
    new_df = df.copy()
    df_did_precourse=new_df[new_df['test preparation course'].values == "completed"]
    return df_did_precourse
##fifth task
def avarage_scores(df: pd.DataFrame) -> pd.DataFrame:   
    new_df = df.copy()
    groupby = new_df.groupby('parental level of education')
    avarage_scores = groupby[['math score', 'reading score', 'writing score']].mean()
    return avarage_scores
##sixth task
def add_age(df: pd.DataFrame):   
    new_df = df.copy()
    np.random.seed(42)
    ages = np.random.randint(18, 67, size=len(new_df))
    new_df['age'] = ages
    return new_df
##seventh task 
def female_top_score(df: pd.DataFrame) -> tuple:    
    new_df = df.copy()
    female_df= new_df[new_df['gender']=='female']
    tuple_max = (female_df['math score'].max(),female_df['reading score'].max(),female_df['writing score'].max())
    return tuple_max
##eighth task
def add_grade(df: pd.DataFrame) -> pd.DataFrame:   
    new_df = df.copy()        
    def get_grade(percentage):
        if percentage >= 0.9:
            return 'A'
        elif percentage >= 0.8:
            return 'B'
        elif percentage >= 0.7:
            return 'C'
        elif percentage >= 0.6:
            return 'D'
        else:
            return 'F'
    new_df['grade'] =((new_df['math score'] + new_df['reading score'] + new_df['writing score']) / 300).apply(get_grade)
    return new_df
##ninth task
def math_bar_plot(df):
    df = pd.DataFrame(df)
    new_df = df.copy()
    fig, ax = plt.subplots()
    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    grouped_data = new_df.groupby('gender').mean(numeric_only=True)
    ax.bar(grouped_data.index, grouped_data['math score']) 
    return fig
##tenth task
def writing_hist(df: pd.DataFrame):   
    new_df = df.copy()
    fig, ax = plt.subplots(figsize=(8,6))
    ax.hist(new_df['writing score'], bins=20, color='#5E86C1')
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')       
    return fig
##eleventh task
def ethnicity_pie_chart(df):
    counts = df['race/ethnicity'].value_counts()
    percentages = counts / counts.sum() * 100
    fig, ax = plt.subplots()
    ax.set_title('Proportion of Students by Race/Ethnicity')
    ax.pie(percentages,
           labels=percentages.index,
           autopct='%1.1f%%')
    return fig