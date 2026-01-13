import pandas as pd

df = pd.read_csv("../data/sales_data_sample.csv", encoding="latin1")

# Convert date column
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Handle missing values
df['STATE'].fillna('Unknown', inplace=True)
df['POSTALCODE'].fillna('Unknown', inplace=True)
df['TERRITORY'].fillna('Unknown', inplace=True)

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Save cleaned data
df_cleaned.to_csv("../data/cleaned_sales_data.csv", index=False)

df_cleaned.head()
