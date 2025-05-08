import pandas as pd

# Correct function name: read_csv, not read.csv
df = pd.read_csv('input.csv')

df['Age in 5 Years'] = df['Age'] + 5

#df.to_csv('output.csv', index=False)

print("Processed data written to output.csv:")
ccd = pd.read_csv('data_ecommerce_customer_churn.csv')
ccd.to_csv('output.csv', index=False)

print(ccd.head(5))