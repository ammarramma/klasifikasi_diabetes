import pandas as pd

data = pd.read_csv('laptops_raw.csv')

chosen_columns = [
    'processor_brand',
    'processor_tier',
    'brand',
    'Price',
    'num_cores',
    'num_threads',
    'ram_memory',
    'primary_storage_capacity',
    'gpu_brand',
    'gpu_type',
    'display_size'
]

# print(data[chosen_columns].head())

print(data['processor_tier'].unique())
print(data['gpu_brand'].unique())
print(data['processor_brand'].unique())
print(data['gpu_type'].unique())
print(data['primary_storage_type'].unique())
# print(data['processor_tier'].value_counts())
# print(data['gpu_brand'].value_counts())
# print(data['processor_brand'].value_counts())