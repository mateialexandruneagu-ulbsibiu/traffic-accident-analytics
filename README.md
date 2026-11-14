# Traffic Accident Analytics

## Project Overview
This project analyzes over 7.7 million traffic accident records from the US Accidents dataset. The goal is to identify accident patterns, explore contributing factors, and predict accident severity using machine learning.

## Data Source
The sample data used for testing and demonstrating the Traffic Accident Analysis System was based on publicly available healthcare datasets obtained from Kaggle. The data was adapted and simplified to fit the database schema and project requirements.
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

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

## Installation & Usage

### Prerequisites

Make sure you have installed:

- Python 3.10+
- Java 17 (required for PySpark)
- Git
- Tableau Public/Desktop

### Clone the Repository

```bash
git clone https://github.com/mateialexandruneagu-ulbsibiu/traffic-accident-analytics
cd traffic-accident-analytics
```

# Conference Presentation

The project was presented at ADEConf 2026 – Advancing Digital Education: Content, Context and Artificial Intelligence, organized by the Faculty of Philosophy, University of Novi Sad, Serbia, on 12–14 November 2026.

The presentation, titled "Learning from Real-World Data: Traffic Accident Analytics as an Applied Case Study in Digital Education", explored how big data analytics, machine learning, and interactive visualization can support practical learning experiences and connect technology with real-world problems.

The presentation highlighted the educational potential of combining authentic datasets, scalable data processing, artificial intelligence, and data visualization to encourage critical thinking and digital literacy.


## Author
Matei-Alexandru Neagu
