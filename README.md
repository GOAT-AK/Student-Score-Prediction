# Student-Score-Prediction
This project focuses on predicting students’ exam performance based on multiple academic, personal, and socio-economic factors. Using machine learning (Linear Regression)

# Table of Content

* [Brief](#Brief)  
* [DataSet](#DataSet)  
* [How_It_Works](#How_It_Works)  
* [Tools](#Tools)  
* [Remarks](#Remarks)  
* [Usage](#Usage)  
* [Sample_Run](#Sample_Run)


# Brief

With the growing emphasis on data-driven education, predicting students’ performance can provide valuable insights for teachers, parents, and institutions.  
This project builds a **machine learning model** to predict student exam scores based on academic, personal, and socio-economic factors.

The goal is to help in:  
- Early identification of students at risk  
- Personalized study recommendations  
- Data-supported educational planning


# DataSet

The dataset used in this project is the [Student Performance Factors](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors) from Kaggle. This dataset provides a comprehensive overview of various factors affecting student performance in exams. It includes information on **study habits, attendance, parental involvement, and other aspects influencing academic success**.  


### Column Descriptions

| Attribute                  | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Hours_Studied              | Number of hours spent studying per week.                                   |
| Attendance                 | Percentage of classes attended.                                            |
| Parental_Involvement       | Level of parental involvement in the student's education (Low, Medium, High). |
| Access_to_Resources        | Availability of educational resources (Low, Medium, High).                 |
| Extracurricular_Activities | Participation in extracurricular activities (Yes, No).                    |
| Sleep_Hours                | Average number of hours of sleep per night.                                |
| Previous_Scores            | Scores from previous exams.                                                |
| Motivation_Level           | Student's level of motivation (Low, Medium, High).                         |
| Internet_Access            | Availability of internet access (Yes, No).                                 |
| Tutoring_Sessions          | Number of tutoring sessions attended per month.                            |
| Family_Income              | Family income level (Low, Medium, High).                                   |
| Teacher_Quality            | Quality of the teachers (Low, Medium, High).                               |
| School_Type                | Type of school attended (Public, Private).                                 |
| Peer_Influence             | Influence of peers on academic performance (Positive, Neutral, Negative).  |
| Physical_Activity          | Average number of hours of physical activity per week.                     |
| Learning_Disabilities      | Presence of learning disabilities (Yes, No).                               |
| Parental_Education_Level   | Highest education level of parents (High School, College, Postgraduate).   |
| Distance_from_Home         | Distance from home to school (Near, Moderate, Far).                        |
| Gender                     | Gender of the student (Male, Female).                                      |
| Exam_Score                 | Final exam score (Target variable).     


# How_It_Works

- Load and clean the dataset (handle missing values, encode categorical features, scale numerical ones).  
- Perform **Exploratory Data Analysis (EDA)** and run **ANOVA tests** to check feature importance.  
- Train a **Linear Regression model** and evaluate it with **MAE, RMSE, R², and accuracy**.  
- Save the model, scaler, and encoders using **pickle**.  
- Deploy a **Streamlit web app** where users input student details and get real-time predictions.


# Tools & Libraries

I. Jupyter Notebook & VS Code  
II. Python 3.x  
III. pandas, numpy  
IV. matplotlib, seaborn  
V. scikit-learn  
VI. pickle  
VII. Streamlit 



# Remarks
* This Python program was run and tested in Jupyter Notebook.
* Ensure the required libraries are installed by running:

  ```bash
  pip install pandas numpy scikit-learn matplotlib seaborn streamlit

# Usage

To begin utilizing this application, follow these steps:

1. Clone this repository:
   
   ```bash
   git clone https://github.com/GOAT-AK/Student-Exam-Score-Prediction

2. Navigate to the cloned repository:

   ```bash
   cd Student-Exam-Score-Prediction

3. Run the Jupyter Notebook:

   ```bash
   Student Score.ipynb

4. Launch the Streamlit app:
   
   ```bash
   streamlit run Script.py


# Sample_Run


* Pic 1

<img width="1042" height="654" alt="Image" src="https://github.com/user-attachments/assets/ded84ee9-f1cc-47b4-be25-6c1cb24e4e0a" />


<hr>


* Pic 2

<img width="995" height="521" alt="Image" src="https://github.com/user-attachments/assets/6c14b475-ea9e-4cb9-9095-768e8f19b0d6" />
   
