import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("MODULE 8 HANDS-ON: DATA ANALYSIS MINI PROJECT")
print("-" * 60)

# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------
print("\n1. LOADING DATA")

df = pd.read_csv("../DATASET/sales_data.csv")

print("\nDataset Preview:")
print(df.head())


# --------------------------------------------------
# 2. DATA CLEANING
# --------------------------------------------------
print("\n2. DATA CLEANING")

print("\nChecking missing values:")
print(df.isnull().sum())

df.dropna(inplace=True)

print("Missing values removed (if any)")


# --------------------------------------------------
# 3. DATA TRANSFORMATION
# --------------------------------------------------
print("\n3. DATA TRANSFORMATION")

df["Total_Value"] = df["Sales"] + df["Profit"]

print("\nTransformed Data:")
print(df.head())


# --------------------------------------------------
# 4. DATA ANALYSIS
# --------------------------------------------------
print("\n4. DATA ANALYSIS")

total_sales = df["Sales"].sum()
avg_profit = df["Profit"].mean()

print("Total Sales:", total_sales)
print("Average Profit:", avg_profit)

print("\nSales by Category:")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)


# --------------------------------------------------
# 5. NUMPY USAGE
# --------------------------------------------------
print("\n5. NUMPY OPERATIONS")

sales_array = np.array(df["Sales"])

print("Max Sales:", np.max(sales_array))
print("Min Sales:", np.min(sales_array))
print("Mean Sales:", np.mean(sales_array))


# --------------------------------------------------
# 6. DATA VISUALISATION
# --------------------------------------------------
print("\n6. DATA VISUALISATION")

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.savefig("sales_chart.png")

print("Chart saved as sales_chart.png")


print("\nProject completed successfully.")
