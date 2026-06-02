# Traffic Accident Analytics

## Project Overview
This project analyzes over 7.7 million traffic accident records from the US Accidents dataset. The goal is to identify accident patterns, explore contributing factors, and predict accident severity using machine learning.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- PySpark
- Scikit-Learn
- Tableau
- Git/GitHub

## Dataset
US Accidents Dataset (March 2023 release)

## Project Structure

traffic-accident-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── screenshots/
│
├── preprocess.py
├── eda.py
├── spark_analysis.py
├── train_model.py
├── requirements.txt
└── README.md

## Data Preprocessing
- Removed duplicate records
- Handled missing values
- Created Hour, Day, Month, and Year features
- Reduced dataset to relevant columns

## Exploratory Data Analysis
- Top accident-prone states
- Accident frequency by hour
- Severity distribution
- Weather condition analysis

## Big Data Processing
PySpark was used to process and analyze the large dataset containing over 7.7 million records.

## Machine Learning
A Random Forest Classifier was trained to predict accident severity.

## Dashboard
An interactive Tableau dashboard was created to visualize:
- Total accidents
- Top states
- Severity distribution
- Hourly accident trends
- Accident density by state

## Key Findings
- Severity level 2 accidents dominate the dataset.
- Certain states experience significantly more accidents than others.
- Accident frequency peaks during commuting hours.
- Weather conditions influence accident severity.

## Author
Matei Neagu
