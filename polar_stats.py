# %%
import numpy as np 
import pandas as pd 
import polars as pl
from polars import Float64, Float32, Int64, Int32, Int16, Int8, UInt64, UInt32, UInt16, UInt8
import matplotlib.pyplot as plt 
import csv
import os 
import math 

from collections import defaultdict, Counter

# %%
os.chdir("C:\Research Task 4")

# %%
insurance_df = pl.read_csv(r"medical_insurance.csv")
netflix_df = pl.read_csv(r"netflix_customer_churn.csv")
social_media_df = pl.read_csv(r"social_media_engagement1.csv")

# %%
# Helper function to identify numeric dtypes
def is_numeric_dtype(dtype):
    return dtype in {Float64, Float32, Int64, Int32, Int16, Int8, UInt64, UInt32, UInt16, UInt8}

# %%
# Define the Polars analysis function
def analyze_dataframe_with_polars(df: pl.DataFrame):
    # Identify numeric and non-numeric columns
    numeric_cols = [col for col, dtype in df.schema.items() if is_numeric_dtype(dtype)]
    non_numeric_cols = [col for col, dtype in df.schema.items() if not is_numeric_dtype(dtype)]

    # Numeric stats
    numeric_stats = df.select(numeric_cols).describe().transpose(include_header=True)
    numeric_stats = numeric_stats.rename({"column": "Metric"})
    numeric_stats = numeric_stats.with_columns([pl.lit("Numeric").alias("Type")])

    # Non-numeric stats
    non_numeric_stats = []
    for col in non_numeric_cols:
        col_df = df.select(pl.col(col)).drop_nulls()
        if col_df.is_empty():
            most_freq_val = None
            most_freq_count = None
        else:
            vc = df.select([pl.col(col)]).drop_nulls().group_by(col).agg(pl.len().alias("count")).sort("count", descending=True)
            most_freq_val = vc[0, col]
            most_freq_count = vc[0, "count"]
        non_numeric_stats.append({
            "Column": col,
            "Type": "Non-Numeric",
            "Count": df.select(pl.col(col)).drop_nulls().height,
            "Unique Values": df.select(pl.col(col)).n_unique(),
            "Most Frequent": most_freq_val,
            "Frequency": most_freq_count
        })

    df_non_numeric_stats = pl.DataFrame(non_numeric_stats)

    return numeric_stats, df_non_numeric_stats

# %%
insurance_num, insurance_non_num = analyze_dataframe_with_polars(insurance_df)
netflix_num, netflix_non_num = analyze_dataframe_with_polars(netflix_df)
social_media_num, social_media_non_num = analyze_dataframe_with_polars(social_media_df)

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


