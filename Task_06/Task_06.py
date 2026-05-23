import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Cleaned Dataset

df = pd.read_csv("cleaned_digital_burnout_dataset.csv")

# Better plot style
sns.set_style("whitegrid")

# Increase overall figure quality
plt.rcParams['figure.figsize'] = (10, 6)

# Check Column Names

print(df.columns)

# Visualization 1: Histogram

plt.figure()

sns.histplot(df['daily_screen_time'], bins=20, kde=True)

plt.title("Distribution of Screen Time Hours")
plt.xlabel("Screen Time Hours")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram_screen_time.png", dpi=300)
plt.show()

# Visualization 2: Scatter Plot

plt.figure()

sns.scatterplot(
    x='daily_screen_time',
    y='productivity_score',
    data=df
)

plt.title("Screen Time vs Productivity Score")
plt.xlabel("Screen Time Hours")
plt.ylabel("Productivity Score")

plt.tight_layout()
plt.savefig("scatter_plot_productivity.png", dpi=300)
plt.show()

# Visualization 3: Heatmap

plt.figure(figsize=(14,10))

# Only numerical columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("heatmap_correlation.png", dpi=300)
plt.show()

# Visualization 4: Bar Chart

# If Work_Mode became encoded after Task 5,
# this plot will still work

plt.figure()

df['work_mode'].value_counts().plot(
    kind='bar'
)

plt.title("Count of Work Modes")
plt.xlabel("Work Mode")
plt.ylabel("Count")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("bar_chart_workmode.png", dpi=300)
plt.show()

# Visualization 5: Boxplot

plt.figure()

sns.boxplot(
    y=df['stress_level']
)

plt.title("Boxplot of Stress Level")
plt.ylabel("Stress Level")

plt.tight_layout()
plt.savefig("boxplot_stress_level.png", dpi=300)
plt.show()

print("All plots generated and saved successfully.")
