# Uber Fares Dataset Analysis

## Overview
This project analyzes Uber ride fare data to uncover patterns in pricing, distance, and time-based trends. It combines Python (for data cleaning and feature engineering) with Power BI (for interactive dashboards) to deliver actionable insights.

## Objectives
- Clean and preprocess the raw Uber dataset.
- Perform exploratory data analysis (EDA) to identify patterns and anomalies.
- Engineer new features (distance, peak/off-peak indicators, time features).
- Visualize results in an interactive Power BI dashboard.
- Provide data-driven recommendations based on findings.

## Dataset
- **Source:** [Kaggle Uber Fares Dataset](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)
- **Files:**
  - `cleaned_uber_fares.csv` — cleaned dataset after removing outliers and missing values.
  - `enhanced_uber_fares.csv` — dataset with additional features (hour, day, distance, peak indicators).

## Methodology
### 1. Data Cleaning (Python)
- Removed missing values and unrealistic coordinates.
- Filtered out negative fares and impossible passenger counts.

### 2. Feature Engineering (Python)
- Extracted hour, day, month, and day of week from timestamps.
- Calculated ride distance using Haversine formula.
- Classified trips into Peak and Off-Peak times.

### 3. Exploratory Data Analysis (Python)
- Fare distribution (histogram, box plot).
- Fare vs distance (scatterplot).
- Average fare by hour and day of week (line and bar charts).
- Peak vs off-peak fare comparison.

### 4. Power BI Dashboard
- Interactive dashboard with filters (month, day of week, peak/off-peak).
- Visuals:
  - Fare distribution
  - Fare vs distance
  - Average fare by hour
  - Average fare by day of week
  - Peak vs off-peak comparison

## Deliverables
- `Uber_Fares_Dashboard.pbix` (interactive Power BI dashboard)
- Cleaned and enhanced datasets (CSV files)
- Screenshots documenting analysis process and dashboard stages
- README (this file)

## How to View Dashboard
1. Download `Uber_Fares_Dashboard.pbix` from this repository.
2. Open with [Power BI Desktop](https://powerbi.microsoft.com/desktop/).

## Insights Summary
- Majority of fares are under $20; a few outliers exceed $100.
- Longer trips correlate strongly with higher fares.
- Peak hours (6-9 AM, 4-7 PM) show slightly elevated average fares.
- Weekend trips tend to be longer and costlier.

## Author
- **Willy Hirwa**
- AUCA — Introduction to Big Data Course
