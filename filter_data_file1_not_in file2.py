import pandas as pd

# Read CSV files
df1 = pd.read_csv(r"C:\Users\Aroha\Desktop\23_06_2024\loan_dpd_data.csv")
df2 = pd.read_csv(r"C:\Users\Aroha\Desktop\23_06_2024\prescription_data.csv")

# Merge DataFrames on loan_number and loan_account_number
merged = pd.merge(df1, df2, left_on='loan_number', right_on='loan_account_number', how='left', indicator=True)

# Filter rows only in df1 (left_only)
result = merged[merged['_merge'] == 'left_only'].drop('_merge', axis=1)

# Print or save the filtered result
print("\nRows in df1 not in df2:")
# print(result)
result.to_csv(r"C:\Users\Aroha\Desktop\23_06_2024\not_fall_under_ncn_data.csv", index=False)