import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load reducer output
data = pd.read_csv("reducer_output.csv", sep="\t", names=["Metric", "Average"])
grouped_data = data.groupby("Metric")

# Statistical Tests
for metric, group in grouped_data:
    if metric in ["ProductQuality", "ServiceQuality", "PurchaseFrequency"]:
        high_avg = group[group["Metric"] == "high"]["Average"]
        low_avg = group[group["Metric"] == "low"]["Average"]
        t_stat, p_val = ttest_ind(high_avg, low_avg)
        print(f"{metric}: t-stat = {t_stat:.2f}, p-value = {p_val:.3f}")

# Visualization
plt.bar(data["Metric"], data["Average"], color="skyblue")
plt.title("Average Scores by Metric")
plt.xlabel("Metric")
plt.ylabel("Average")
plt.savefig("average_scores.png")

# Demographic Visualizations
country_data = data[data["Metric"] == "Country"]
country_data.plot(kind="pie", y="Average", legend=False, autopct="%1.1f%%", title="Customer Distribution by Country")
plt.savefig("country_distribution.png")
