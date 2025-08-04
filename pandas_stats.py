# %%
import numpy as np 
import pandas as pd 
import polars as pl
import matplotlib.pyplot as plt 
import csv
import os 
import math 

from collections import defaultdict, Counter

# %%
os.chdir("C:\Research Task 4")

# %%
insurance_df = pd.read_csv(r"medical_insurance.csv")
netflix_df = pd.read_csv(r"netflix_customer_churn.csv")
social_media_df = pd.read_csv(r"social_media_engagement1.csv")

# %%
def analyze_dataframe_with_pandas(df):
    # Numeric summary stats
    numeric_stats = df.describe().T.reset_index().rename(columns={"index": "Column"})
    numeric_stats["Type"] = "Numeric"

    # Non-numeric summary stats
    non_numeric_stats = []
    for col in df.select_dtypes(include=['object']).columns:
        value_counts = df[col].value_counts(dropna=True)
        most_freq_val = value_counts.index[0] if not value_counts.empty else None
        most_freq_count = value_counts.iloc[0] if not value_counts.empty else None
        non_numeric_stats.append({
            "Column": col,
            "Type": "Non-Numeric",
            "Count": df[col].count(),
            "Unique Values": df[col].nunique(),
            "Most Frequent": most_freq_val,
            "Frequency": most_freq_count
        })

    df_non_numeric_stats = pd.DataFrame(non_numeric_stats)

    return numeric_stats, df_non_numeric_stats

# %%
insurance_num, insurance_non_num = analyze_dataframe_with_pandas(insurance_df)
netflix_num, netflix_non_num = analyze_dataframe_with_pandas(netflix_df)
social_media_num, social_media_non_num = analyze_dataframe_with_pandas(social_media_df)

# %%
insurance_num

# %%
insurance_non_num

# %%
netflix_num

# %%
netflix_non_num

# %%
social_media_num

# %%
social_media_non_num


