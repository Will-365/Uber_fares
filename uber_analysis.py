import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load enhanced dataset
df = pd.read_csv("enhanced_uber_fares.csv")

# 1. Fare distribution
plt.figure(figsize=(8,5))
sns.histplot(df['fare_amount'], bins=50, kde=True)
plt.title('Fare Amount Distribution')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.savefig('fare_distribution.png')  # Save for report
plt.show()

# 2. Boxplot to detect fare outliers
plt.figure(figsize=(6,4))
sns.boxplot(x=df['fare_amount'])
plt.title('Fare Amount Outliers')
plt.savefig('fare_boxplot.png')
plt.show()

# 3. Fare vs Distance
plt.figure(figsize=(8,5))
sns.scatterplot(x='distance_km', y='fare_amount', data=df, alpha=0.3)
plt.title('Fare vs Distance')
plt.xlabel('Distance (km)')
plt.ylabel('Fare ($)')
plt.savefig('fare_vs_distance.png')
plt.show()

# 4. Average fare by hour of day
hourly_fare = df.groupby('hour')['fare_amount'].mean()
plt.figure(figsize=(8,5))
hourly_fare.plot(kind='line', marker='o')
plt.title('Average Fare by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Average Fare ($)')
plt.savefig('avg_fare_by_hour.png')
plt.show()

# 5. Average fare by day of week (innovative)
plt.figure(figsize=(8,5))
sns.barplot(x='day_of_week', y='fare_amount', data=df, estimator='mean', order=[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Average Fare by Day of Week')
plt.savefig('avg_fare_by_day.png')
plt.show()

# 6. Peak vs Off-peak comparison (innovative)
plt.figure(figsize=(6,4))
sns.boxplot(x='peak_time', y='fare_amount', data=df)
plt.title('Fare Amount: Peak vs Off-Peak')
plt.savefig('peak_vs_offpeak.png')
plt.show()
