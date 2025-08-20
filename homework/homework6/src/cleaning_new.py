import pandas as pd, numpy as np
from sklearn.preprocessing import MinMaxScaler

def missing_median_( df, columns = None):
    df_copy = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns #includes only columns with numeric dtype
    else: print("All columns selected.")
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy

def drop_missing(df, columns=None, threshold=None):
    df_copy = df.copy()
    if columns is not None:
        return df_copy.dropna(subset=columns)
    if threshold is not None:
        return df_copy.dropna(thresh=int(threshold*df_copy.shape[1]))
    return df_copy.dropna()
    
def normalize_data(df, columns=None, method='minmax'):
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    if method=='minmax':
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy

def correct_column_types(df):
    df_copy = df.copy()
    if 'price' in df_copy.columns:
        df_copy['price'] = df_copy['price'].str.replace('$','').astype(float)
    if 'date_str' in df_copy.columns:
        df_copy['date'] = pd.to_datetime(df_copy['date_str'], errors='coerce')
    if 'category' in df_copy.columns:
        df_copy['category'] = df_copy['category'].str.lower().astype('category')
    return df_copy

def compare_raw_vs_processed(raw_df, processed_df):
    print("Shape Comparison:")
    print(f"Raw shape:       {raw_df.shape}")
    print(f"Processed shape: {processed_df.shape}")
    print()

    print(" Missing Values (Raw):")
    print(raw_df.isna().sum())
    print()

    print(" Missing Values (Processed):")
    print(processed_df.isna().sum())
    print()

    print("Dtypes Comparison:")
    print(pd.DataFrame({
        "raw_dtype": raw_df.dtypes,
        "processed_dtype": processed_df.dtypes
    }))
    print()

   