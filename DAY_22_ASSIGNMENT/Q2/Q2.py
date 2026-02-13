import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")

df["Total"] = df["Quantity"] * df["Price"]

totals = df["Total"].values

total_sales = np.sum(totals)
avg_sales = np.mean(totals)
std_sales = np.std(totals)

print("Total Sales:", total_sales)
print("Average Daily Sales:", round(avg_sales, 2))
print("Standard Deviation:", round(std_sales, 2))

best_product = df.loc[df["Quantity"].idxmax()]

print("Best Selling Product:", best_product["Product"])
print("Quantity Sold:", best_product["Quantity"])