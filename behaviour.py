import pandas as pd
import numpy as np  
import database
df=pd.read_excel('customer_shopping.csv.xlsx')
df.head()
df.describe(include='all') #to give summary about data
df["Review Rating"] = df.groupby('Category')["Review Rating"].transform(lambda x: x.fillna(x.mean()))
df.isnull().sum()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('(', '')
df.columns = df.columns.str.replace(')', '')
df= df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'}) #this name doesnt change that is why did this
labels=["Young Age","Adult","Middle Age","Senoir"]
df["age_group"] = pd.qcut(df["age"], q=4, labels=labels) # dividing age into grp as per labels
frequency_mapping={
    "Fortnightly":14,
    "Weekly":7,
    "Monthly":30,
    "Quarterly":90,
    "Bi-Weekly":14,
    "Annually":365,
    "Every 3 Months":90
}
df["purchase_frequency_days"]=df["frequency_of_purchases"].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']]
df=df.drop('promo_code_used',axis=1) # both discount and prormo code is same that is why removed one of them
database.insert_data(df)
result = database.run_query("SELECT * FROM customers LIMIT 5")
print(result)
query = """
SELECT category, COUNT(*) as total_customers
FROM customers
GROUP BY category
"""
result = database.run_query(query)
print(result) # to show the category wise count of customers
query = """
SELECT gender, SUM(purchase_amount_usd) as revenue
FROM customers
group by gender
""" 
result = database.run_query(query)
print(result) # to show the revenue gender wise