import pandas as pd

df = pd.read_csv("../data/cleaned_sales_data.csv")

# Revenue by Country
revenue_country = df.groupby('COUNTRY')['SALES'].sum().reset_index()

# Revenue by Product Line
revenue_productline = df.groupby('PRODUCTLINE')['SALES'].sum().reset_index()

# Monthly Sales Growth
df['Month'] = pd.to_datetime(df['ORDERDATE']).dt.to_period('M')
monthly_sales = df.groupby('Month')['SALES'].sum().reset_index()

# Export outputs
revenue_country.to_csv("../outputs/revenue_by_country.csv", index=False)
revenue_productline.to_csv("../outputs/revenue_by_productline.csv", index=False)
monthly_sales.to_csv("../outputs/monthly_sales_growth.csv", index=False)
