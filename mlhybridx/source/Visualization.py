import seaborn as sns 
import random
import pandas as pd

def rnd_cols(df): 
        col = df.columns.tolist()
        cols = random.choice(col)
        return cols


def count_plot(df,col_name=''):
    if col_name == '': 
        return sns.countplot(x=df[rnd_cols(df)])
    else:
        return sns.countplot(x=df[col_name])
    
def box_plot(df,col_name=''):
    if col_name == '': 
        return sns.boxplot(df[rnd_cols(df)])
    else:
        return sns.boxplot(df[col_name])
    
