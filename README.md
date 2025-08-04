# Task_04_Descriptive_Stats

Multi-Dataset Statistics & Aggregation
This repository explores data analysis and aggregation using three different approaches — Pure Python, Pandas, and Polars — across multiple datasets. The goal is to compare readability, performance, and ease of use between native Python and popular data libraries.
Datasets Used
Dataset	Description	Source
Netflix Customer Churn	Customer-level data to explore subscription cancellation behavior.	Kaggle - Netflix Churn

Social Media Engagement	Engagement metrics (likes, views, comments, etc.) across platforms.	Kaggle - Social Media Engagement

Medical Insurance	Medical insurance costs and user features (age, BMI, region, etc.)	Kaggle - Health Insurance

________________________________________
 Notebooks Overview
1. pure_python_stats.py
•	Uses core python to:
o	Load and parse CSV files manually
o	Perform: Basic statistics (mean, min, max, std, median) for numeric columns
o	Results are saved as dataframes.
2. pandas_stats.py
•	Uses the Pandas library to:
o	Load and analyze all three datasets.
o	Produce basic reports about the datasets.
o	Compute detailed descriptive statistics
3. polars_stats.py
•	Uses the Polars library for high-performance data processing.
•	Performs the same report logic as pandas_stats.py, but using Polars' syntax and performance optimizations.
________________________________________
 How to Run
1.	Make sure you have Python 3.7+ installed.
2.	Install dependencies:
pip install pandas polars jupyter
3.	Clone or download this repository to your local system.
4.	Important: Navigate to the directory where you've saved both the dataset and the notebooks:
cd path/to/your/local/folder
Replace path/to/your/local/folder with the actual path on your machine.
5.	Start Jupyter:
jupyter notebook
6.	Open and run pure_python_stats.py, pandas_stats.py or polars_stats.py.
________________________________________ Summary of Findings
Q: Was it a challenge to produce identical results without using a library? If so, describe the challenge and how you overcame it.
A: Yes, replicating results without libraries like pandas or polars proved difficult due to the lack of abstraction in pure Python. Achieving identical outcomes was challenging without leveraging specialized data processing tools.
________________________________________
Q: Do you find one approach easier or more performant?
A: Yes, Polars delivered the best performance, especially on large datasets. Pandas offered the most balanced combination of usability and speed. Compared to pure Python, both pandas and polars were significantly easier and more efficient.
________________________________________
Q: If you were coaching a junior data analyst, what approach would you recommend?
A: I would advise a junior data analyst to begin with pandas due to its simplicity and robust capabilities, and later explore polars for tasks where performance is critical.
________________________________________
Q: Can coding AI such as ChatGPT produce recommendations such as template code to jump start each approach?
A: Definitely. Tools like ChatGPT are well-suited for generating template code specific to different data analysis methods, making it easier to get started.
________________________________________
Q: What default approach do these kinds of tools recommend when asked to produce descriptive statistics?
A: These tools usually suggest using pandas when generating descriptive statistics.
Q: Do you agree with these recommendations? Why or why not?
A: Yes, I do agree — especially for general analytical tasks.
✅ Reasons for agreement:
•	pandas offers sufficient speed for most scenarios and is much simpler than coding aggregations manually.
•	Its syntax is intuitive, and methods like .describe() provide a comprehensive summary.
•	AI-generated code using pandas is typically accurate, succinct, and user-friendly for beginners or intermediate users. In rare cases, outputs may need review.

