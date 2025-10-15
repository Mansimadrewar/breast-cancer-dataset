# breast-cancer-dataset
🩺 Breast Cancer Classification using Machine Learning
📘 Project Overview

Breast cancer is one of the most common cancers worldwide. Early detection through classification of tumors into benign (non-cancerous) or malignant (cancerous) can save lives.
This project applies machine learning algorithms to predict the nature of a tumor based on clinical features derived from cell nuclei present in breast mass tissue.

🧠 Objective

To build and evaluate a machine learning model that can accurately classify breast cancer tumors using the Breast Cancer Wisconsin (Diagnostic) Dataset.

📂 Dataset Information

Source: Kaggle - Breast Cancer Dataset

The dataset includes features such as:

radius_mean

texture_mean

perimeter_mean

area_mean

smoothness_mean

compactness_mean

and many more morphological characteristics of cell nuclei.

Each sample is labeled as either:

0 → Benign

1 → Malignant

⚙️ Steps and Methodology

Importing and Exploring Data

Loaded the dataset using Pandas

Checked for null values and performed descriptive analysis

Data Preprocessing

Feature selection

Splitting data into training and test sets

Normalization / scaling

Model Building

Implemented classification models such as Support Vector Machine (SVM)

Tuned hyperparameters to optimize performance

Model Evaluation

Accuracy, Precision, Recall, F1-score

Confusion Matrix visualization

🧩 Technologies Used

Python 3

NumPy

Pandas

Matplotlib / Seaborn

Scikit-learn

KaggleHub (for dataset download)

📈 Results

Achieved high accuracy in predicting tumor types using SVM.

Model demonstrated strong precision and recall, minimizing false negatives.
