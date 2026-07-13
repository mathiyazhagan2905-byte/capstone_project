import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Create plots folder
os.makedirs("plots", exist_ok=True)

# Load dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Rename target column
df.rename(columns={"MedHouseVal": "HousePrice"}, inplace=True)

# Create a categorical column
df["IncomeCategory"] = pd.cut(
    df["MedInc"],
    bins=[0, 2, 4, 6, 20],
    labels=["Low", "Medium", "High", "Very High"]
)

# -----------------------------
# Basic Information
# -----------------------------
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nSummary Statistics")
print(df.describe())

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(8,5))
df["HousePrice"].hist(bins=30)
plt.title("House Price Distribution")
plt.xlabel("House Price")
plt.ylabel("Frequency")
plt.savefig("plots/house_price_histogram.png")
plt.close()

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["MedInc"], df["HousePrice"], alpha=0.3)
plt.xlabel("Median Income")
plt.ylabel("House Price")
plt.title("Income vs House Price")
plt.savefig("plots/income_vs_price.png")
plt.close()

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure(figsize=(7,5))
df["IncomeCategory"].value_counts().plot(kind="bar")
plt.title("Income Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.savefig("plots/income_category.png")
plt.close()

# -----------------------------
# Correlation Heatmap
# -----------------------------
corr = df.select_dtypes(include="number").corr()

plt.figure(figsize=(10,8))
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png")
plt.close()

print("\nEDA Completed Successfully!")