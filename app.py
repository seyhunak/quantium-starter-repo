import pandas as pd
import glob

# Get all CSV files in the data folder
csv_files = glob.glob("data/*.csv")

# Load them into a list of DataFrames
dfs = [pd.read_csv(file) for file in csv_files]

processed_dfs = []

for df in dfs:
    # Filter Pink Morsels
    df = df[df['product'] == 'Pink Morsel']
    
    # Calculate sales
    df['Sales'] = df['quantity'] * df['price']
    
    # Keep only required columns
    df = df[['Sales', 'date', 'region']].copy()
    
    # Rename columns if necessary
    df.rename(columns={'date': 'Date', 'region': 'Region'}, inplace=True)
    
    processed_dfs.append(df)

final_df = pd.concat(processed_dfs, ignore_index=True)
final_df.to_csv('data/processed_sales.csv', index=False)
print("Data processing complete! File saved as 'processed_sales.csv'.")