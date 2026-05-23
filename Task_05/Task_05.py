import pandas as pd
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("/content/digital_burnout_productivity_dataset_5M (1).csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Check Missing Values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Handle missing values

for column in df.columns:
    if df[column].dtype == 'object':
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:
        df[column].fillna(df[column].mean(), inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Remove Duplicate Rows

print("\nNumber of Duplicate Rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicate Rows Removed.")

# Show Dataset Statistics

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Encode Categorical Columns

label_encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = label_encoder.fit_transform(df[column])

print("\nCategorical Columns Encoded Successfully.")

# Save Cleaned Dataset

df.to_csv("cleaned_digital_burnout_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")
