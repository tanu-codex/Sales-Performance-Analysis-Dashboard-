import pandas as pd
import matplotlib.pyplot as plt

# 1. Create monthly sales dataset
data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ],
    "Sales": [
        12000, 15000, 18000, 14000,
        22000, 25000, 20000, 28000,
        30000, 26000, 35000, 40000
    ]
}

df = pd.DataFrame(data)

# 2. Calculate sales statistics
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
highest_month = df.loc[df["Sales"].idxmax(), "Month"]
highest_sales = df["Sales"].max()
lowest_month = df.loc[df["Sales"].idxmin(), "Month"]

# 3. Display dashboard summary
print("=" * 40)
print(" MONTHLY SALES PERFORMANCE DASHBOARD ")
print("=" * 40)

print("Total Sales: Rs.", total_sales)
print("Average Monthly Sales: Rs.", round(average_sales, 2))
print("Highest Sales Month:", highest_month)
print("Highest Sales: Rs.", highest_sales)
print("Lowest Sales Month:", lowest_month)

print("\nMONTHLY SALES DATA")
print(df.to_string(index=False))

# 4. Create dashboard graphs
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart
axes[0].bar(df["Month"], df["Sales"])
axes[0].set_title("Monthly Sales Comparison")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales (Rs.)")

# Line chart
axes[1].plot(
    df["Month"], df["Sales"], marker="o"
)
axes[1].set_title("Monthly Sales Trend")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Sales (Rs.)")
axes[1].grid(True)

plt.tight_layout()
plt.show()

# 5. Save dataset as CSV
df.to_csv("monthly_sales.csv", index=False)

print("\nDataset saved as monthly_sales.csv")