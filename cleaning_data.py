import pandas as pd

df = pd.read_csv('laptops_raw.csv')

# Drop rows with missing values
df = df.dropna().copy()

# Convert price to rupiah (assuming original price is in INR)
kurs_inr_to_idr = 190
df['Price'] = df['Price'] * kurs_inr_to_idr

df.to_csv('laptops_cleaned.csv', index=False)