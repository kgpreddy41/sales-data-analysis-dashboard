import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("data/sales_data.csv")

print("========== SALES DATA ANALYSIS ==========")

# 1. Display first 5 records
print("\nFirst 5 records:")
print(df.head())

# 2. Dataset information
print("\nDataset Information:")
print(df.info())

# 3. Number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 6. Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 7. Basic sales statistics
print("\n========== SALES SUMMARY ==========")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity:", total_quantity)
print("Total Orders:", total_orders)

# 8. Category-wise sales
print("\n========== CATEGORY-WISE SALES ==========")

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print(category_sales)

# 9. Region-wise sales
print("\n========== REGION-WISE SALES ==========")

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print(region_sales)

# 10. Product-wise sales
print("\n========== TOP 10 PRODUCTS ==========")

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print(product_sales.head(10))

# 11. Monthly sales
df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

# 12. Category-wise profit
print("\n========== CATEGORY-WISE PROFIT ==========")

category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print(category_profit)

# 13. Save cleaned data
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")

# 14. Sales by category chart
plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("data/sales_by_category.png")

plt.show()

print("\nAnalysis completed successfully!")